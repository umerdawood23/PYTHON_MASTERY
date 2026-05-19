const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  ImageRun, AlignmentType, HeadingLevel, LevelFormat, BorderStyle,
  WidthType, ShadingType, PageBreak
} = require("docx");
const fs = require("fs");
const path = require("path");

// ── Colors ─────────────────────────────────────────────────────────
const NAVY    = "0B1F3A";
const GOLD    = "D4A843";
const RED     = "DC2626";
const AMBER   = "D97706";
const GREEN   = "059669";
const MUTED   = "6B7280";
const LIGHT   = "F3F4F6";
const WHITE   = "FFFFFF";

// ── Image dimensions (px at 96dpi → EMU = px * 9144) ──────────────
const diagW = 700, contentInches = 6.5;

// ── Helpers ────────────────────────────────────────────────────────
function spacer(pts = 120) {
  return new Paragraph({ children: [], spacing: { before: pts, after: 0 } });
}

function hr(color = "E5E7EB") {
  return new Paragraph({
    children: [new TextRun("")],
    border: { bottom: { style: BorderStyle.SINGLE, size: 4, color, space: 1 } },
    spacing: { before: 80, after: 80 },
  });
}

function h2(text, color = NAVY) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    children: [new TextRun({ text, bold: true, font: "Arial", size: 28, color })],
    spacing: { before: 280, after: 100 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: GOLD, space: 4 } },
  });
}

function h3(text, color = NAVY) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    children: [new TextRun({ text, bold: true, font: "Arial", size: 22, color })],
    spacing: { before: 200, after: 80 },
  });
}

function body(text, opts = {}) {
  return new Paragraph({
    children: [new TextRun({ text, font: "Arial", size: 20, color: opts.color || "374151", bold: opts.bold || false })],
    spacing: { before: 40, after: 40 },
    alignment: opts.align || AlignmentType.LEFT,
  });
}

function bullet(text, opts = {}) {
  const color = opts.color || "374151";
  return new Paragraph({
    numbering: { reference: "bullets", level: 0 },
    children: [
      ...(opts.label ? [new TextRun({ text: opts.label + "  ", bold: true, font: "Arial", size: 20, color: opts.labelColor || NAVY })] : []),
      new TextRun({ text, font: "Arial", size: 20, color }),
    ],
    spacing: { before: 40, after: 40 },
  });
}

function coloredPara(text, bg, textColor = WHITE) {
  return new Paragraph({
    children: [new TextRun({ text: `  ${text}  `, font: "Arial", size: 20, bold: true, color: textColor })],
    shading: { fill: bg, type: ShadingType.CLEAR },
    spacing: { before: 60, after: 60 },
  });
}

// ── Safely Handle Images ───────────────────────────────────────────
function safeImage(imagePath, heightRatio = 0.6) {
  try {
    const data = fs.readFileSync(imagePath);
    return new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 120, after: 40 },
      children: [
        new ImageRun({
          data,
          transformation: { 
            width: Math.round(contentInches * 96), 
            height: Math.round(heightRatio * contentInches * 96) 
          },
          type: "png"
        })
      ]
    });
  } catch (error) {
    // Fallback if image doesn't exist
    return new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 120, after: 40 },
      children: [
        new TextRun({ 
          text: `[ Diagram Placeholder: Provide image at ${imagePath} ]`, 
          font: "Arial", size: 16, color: "DC2626", bold: true 
        })
      ],
      shading: { fill: "FEE2E2", type: ShadingType.CLEAR }
    });
  }
}

function twoColTable(left, right, leftColor = LIGHT, rightColor = LIGHT) {
  const border = { style: BorderStyle.SINGLE, size: 1, color: "E5E7EB" };
  const borders = { top: border, bottom: border, left: border, right: border };
  const cellMargins = { top: 100, bottom: 100, left: 160, right: 160 };
  return new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [4680, 4680],
    rows: [new TableRow({
      children: [
        new TableCell({ borders, width: { size: 4680, type: WidthType.DXA }, shading: { fill: leftColor, type: ShadingType.CLEAR }, margins: cellMargins, children: left }),
        new TableCell({ borders, width: { size: 4680, type: WidthType.DXA }, shading: { fill: rightColor, type: ShadingType.CLEAR }, margins: cellMargins, children: right }),
      ]
    })]
  });
}

function actionTable(rows) {
  const border = { style: BorderStyle.SINGLE, size: 1, color: "E5E7EB" };
  const borders = { top: border, bottom: border, left: border, right: border };
  const m = { top: 80, bottom: 80, left: 120, right: 120 };

  const headerRow = new TableRow({
    children: [
      new TableCell({ borders, width: { size: 3500, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: m, children: [new Paragraph({ children: [new TextRun({ text: "Fix", bold: true, font: "Arial", size: 18, color: WHITE })] })] }),
      new TableCell({ borders, width: { size: 1800, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: m, children: [new Paragraph({ children: [new TextRun({ text: "Impact", bold: true, font: "Arial", size: 18, color: WHITE })] })] }),
      new TableCell({ borders, width: { size: 1530, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: m, children: [new Paragraph({ children: [new TextRun({ text: "Effort", bold: true, font: "Arial", size: 18, color: WHITE })] })] }),
      new TableCell({ borders, width: { size: 2530, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: m, children: [new Paragraph({ children: [new TextRun({ text: "When", bold: true, font: "Arial", size: 18, color: WHITE })] })] }),
    ]
  });

  const dataRows = rows.map((r, i) => {
    const bg = i % 2 === 0 ? WHITE : "F9FAFB";
    return new TableRow({
      children: [
        new TableCell({ borders, width: { size: 3500, type: WidthType.DXA }, shading: { fill: bg, type: ShadingType.CLEAR }, margins: m, children: [new Paragraph({ children: [new TextRun({ text: r[0], font: "Arial", size: 18, color: "1F2937" })] })] }),
        new TableCell({ borders, width: { size: 1800, type: WidthType.DXA }, shading: { fill: bg, type: ShadingType.CLEAR }, margins: m, children: [new Paragraph({ children: [new TextRun({ text: r[1], font: "Arial", size: 18, color: r[2] || "374151", bold: true })] })] }),
        new TableCell({ borders, width: { size: 1530, type: WidthType.DXA }, shading: { fill: bg, type: ShadingType.CLEAR }, margins: m, children: [new Paragraph({ children: [new TextRun({ text: r[3], font: "Arial", size: 18, color: "374151" })] })] }),
        new TableCell({ borders, width: { size: 2530, type: WidthType.DXA }, shading: { fill: bg, type: ShadingType.CLEAR }, margins: m, children: [new Paragraph({ children: [new TextRun({ text: r[4], font: "Arial", size: 18, color: "374151" })] })] }),
      ]
    });
  });

  return new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [3500, 1800, 1530, 2530],
    rows: [headerRow, ...dataRows],
  });
}

// ── BUILD DOCUMENT ─────────────────────────────────────────────────
async function buildDoc() {
  const doc = new Document({
    numbering: {
      config: [
        {
          reference: "bullets",
          levels: [{
            level: 0, format: LevelFormat.BULLET, text: "•",
            alignment: AlignmentType.LEFT,
            style: { paragraph: { indent: { left: 560, hanging: 280 } } }
          }]
        },
        {
          reference: "numbering",
          levels: [{
            level: 0, format: LevelFormat.DECIMAL, text: "%1.",
            alignment: AlignmentType.LEFT,
            style: { paragraph: { indent: { left: 560, hanging: 280 } } }
          }]
        },
      ]
    },
    sections: [{
      properties: {
        page: {
          size: { width: 12240, height: 15840 },
          margin: { top: 1200, right: 1200, bottom: 1200, left: 1200 },
        }
      },
      children: [
        // ── COVER ──────────────────────────────────────────────────
        new Paragraph({
          children: [new TextRun({ text: "MAZAYYAH.COM", bold: true, font: "Arial", size: 52, color: WHITE })],
          shading: { fill: NAVY, type: ShadingType.CLEAR },
          alignment: AlignmentType.CENTER,
          spacing: { before: 400, after: 0 },
        }),
        new Paragraph({
          children: [new TextRun({ text: "CRO & Growth Audit Report", font: "Arial", size: 30, color: GOLD, bold: true })],
          shading: { fill: NAVY, type: ShadingType.CLEAR },
          alignment: AlignmentType.CENTER,
          spacing: { before: 0, after: 0 },
        }),
        new Paragraph({
          children: [new TextRun({ text: "Prepared by Quant Marketing Agency  |  May 2026", font: "Arial", size: 18, color: "93C5FD" })],
          shading: { fill: NAVY, type: ShadingType.CLEAR },
          alignment: AlignmentType.CENTER,
          spacing: { before: 60, after: 280 },
        }),

        spacer(80),

        // ── EXECUTIVE SUMMARY BOX ──────────────────────────────────
        coloredPara("EXECUTIVE SUMMARY", NAVY, GOLD),
        new Paragraph({
          children: [
            new TextRun({ text: "The store has real potential in the KSA market — but it cannot profitably run paid ads today. Several critical issues must be resolved before a single dirham of ad spend is deployed.", font: "Arial", size: 20, color: "1F2937" })
          ],
          shading: { fill: "EFF6FF", type: ShadingType.CLEAR },
          spacing: { before: 0, after: 0 },
          indent: { left: 160, right: 160 },
        }),

        spacer(100),

        // ── SECTION 1 ──────────────────────────────────────────────
        h2("01 — Customer Journey & Funnel Leaks"),
        body("Every paid ad visitor follows this path. Right now, there are four major leak points that kill conversions before a purchase happens."),
        spacer(40),

        safeImage("./diag_funnel.png", 420/700),
        new Paragraph({
          children: [new TextRun({ text: "Fig. 1 — Funnel Friction Map: where visitors are lost today", font: "Arial", size: 16, color: MUTED, italics: true })],
          alignment: AlignmentType.CENTER,
          spacing: { before: 0, after: 120 },
        }),

        h3("What This Means"),
        bullet("The homepage hero shows images with no headline or offer — cold traffic bounces immediately."),
        bullet("Product pages have no reviews, no COD badge, and one has a live AI-prompt artifact in the description."),
        bullet("Arabic is only used in section headers — product content is English only. KSA buyers feel friction."),

        spacer(60),

        // ── SECTION 2 ──────────────────────────────────────────────
        h2("02 — Brand Trust: What's Missing"),
        body("Trust signals are the difference between a visitor and a buyer. Below is what the store has vs. what it needs."),
        spacer(60),

        twoColTable(
          [
            new Paragraph({ children: [new TextRun({ text: "✗  What's Missing", bold: true, font: "Arial", size: 20, color: "991B1B" })], spacing: { before: 0, after: 80 } }),
            new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [new TextRun({ text: "No payment icons (MADA, Apple Pay, COD)", font: "Arial", size: 19, color: "374151" })], spacing: { before: 40, after: 40 } }),
            new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [new TextRun({ text: "No visible return/refund policy", font: "Arial", size: 19, color: "374151" })], spacing: { before: 40, after: 40 } }),
          ],
          [
            new Paragraph({ children: [new TextRun({ text: "✓  Quick Fixes", bold: true, font: "Arial", size: 20, color: "065F46" })], spacing: { before: 0, after: 80 } }),
            new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [new TextRun({ text: "Add MADA / Visa / COD badge row under Add to Cart", font: "Arial", size: 19, color: "374151" })], spacing: { before: 40, after: 40 } }),
            new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [new TextRun({ text: "Add sticky announcement bar: Free ship + COD on every page", font: "Arial", size: 19, color: "374151" })], spacing: { before: 40, after: 40 } }),
          ],
          "FEF2F2", "F0FDF4"
        ),

        spacer(100),
        new Paragraph({ children: [new PageBreak()] }),

        // ── SECTION 3 ──────────────────────────────────────────────
        h2("03 — Copywriting: Features vs. Benefits"),
        body("Every product description on the site describes what the product is — not what the buyer gains. Cold paid traffic needs to feel the benefit immediately or they leave."),
        spacer(40),

        safeImage("./diag_copy.png", 360/700),
        new Paragraph({
          children: [new TextRun({ text: "Fig. 2 — Current copy vs. benefit-led rewrites for three hero products", font: "Arial", size: 16, color: MUTED, italics: true })],
          alignment: AlignmentType.CENTER,
          spacing: { before: 0, after: 120 },
        }),

        h3("The Rewrite Formula"),
        bullet("Step 1:", { label: "Open with the problem:", labelColor: RED }),
        bullet("Step 2:", { label: "Introduce the relief:", labelColor: GREEN }),
        
        spacer(80),
        coloredPara("⚠  URGENT: The Smartwatch product description starts with \"Here's a professional product description for...\" — the raw AI prompt is live on the page. Fix this today.", "FEF3C7", "92400E"),

        spacer(100),
        new Paragraph({ children: [new PageBreak()] }),

        // ── SECTION 6: PRIORITY MATRIX ─────────────────────────────
        h2("06 — Priority Action Matrix"),
        body("Every fix ranked by: how fast it impacts revenue vs. how long it takes to implement."),
        spacer(40),

        safeImage("./diag_matrix.png", 420/700),
        new Paragraph({
          children: [new TextRun({ text: "Fig. 5 — Impact vs. Effort matrix: where to focus your time", font: "Arial", size: 16, color: MUTED, italics: true })],
          alignment: AlignmentType.CENTER,
          spacing: { before: 0, after: 120 },
        }),

        spacer(60),

        actionTable([
          ["Restock or unpublish out-of-stock products",       "🔴 Blocks all ROAS",   RED,   "30 min",  "Today — P0"],
          ["Delete AI prompt text from Smartwatch page",       "🔴 Trust failure",     RED,   "15 min",  "Today — P0"],
          ["Remove fake Sold:150 / Available:150 urgency",     "🔴 Trust failure",     RED,   "20 min",  "Today — P0"],
          ["Verify Meta Pixel events firing correctly",        "🔴 No optimization",   RED,   "1 hour",  "Today — P0"],
          ["Add payment trust badges (MADA, Apple Pay, COD)",  "🟠 High",              AMBER, "2 hours", "Within 72hr"],
        ]),

        spacer(120),
        hr(GOLD),
        new Paragraph({
          children: [new TextRun({ text: "This report is based on a live frontend audit of mazayyah.com conducted May 2026.", font: "Arial", size: 14, color: MUTED, italics: true })],
          alignment: AlignmentType.CENTER,
          spacing: { before: 0, after: 0 },
        }),
      ]
    }]
  });

  const outputPath = path.resolve("./Mazayyah_CRO_Audit_Quant.docx");
  const buf = await Packer.toBuffer(doc);
  fs.writeFileSync(outputPath, buf);
  console.log(`✅ Document saved to: ${outputPath}`);
}

buildDoc().catch(console.error);