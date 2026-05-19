const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, HeadingLevel, BorderStyle, WidthType, ShadingType,
  VerticalAlign, PageBreak, LevelFormat, PageNumber,
  Header, Footer, TabStopType, TabStopPosition
} = require('docx');
const fs = require('fs');

// ─── Brand Colors ─────────────────────────────────────────────────────────
const C = {
  navy:       '0B1F3A',
  gold:       'D4A843',
  green:      '1A7A4A',
  teal:       '0E7490',
  slate:      '2C3E50',
  silver:     'F4F6F8',
  lightGold:  'FDF3DC',
  lightGreen: 'E8F5EE',
  lightBlue:  'EBF3FB',
  white:      'FFFFFF',
  gray:       '6B7280',
  darkGray:   '374151',
  red:        'B91C1C',
  ink:        '1A1A2E',
};

// ─── Border helpers ────────────────────────────────────────────────────────
const bd = (color='CCCCCC', sz=4) => ({ style: BorderStyle.SINGLE, size: sz, color });
const allBd = (color='CCCCCC', sz=4) => ({ top:bd(color,sz), bottom:bd(color,sz), left:bd(color,sz), right:bd(color,sz) });
const noBd = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
const noBds = { top:noBd, bottom:noBd, left:noBd, right:noBd };

// ─── Cell factory ─────────────────────────────────────────────────────────
function cell(text, opts={}) {
  const {
    w=2000, bold=false, bg=null, color=null,
    align=AlignmentType.LEFT, borders=null, size=20,
    valign=VerticalAlign.CENTER, colspan=1, italic=false,
    topPad=100, botPad=100
  } = opts;
  return new TableCell({
    width: { size: w, type: WidthType.DXA },
    columnSpan: colspan,
    verticalAlign: valign,
    shading: bg ? { fill: bg, type: ShadingType.CLEAR } : undefined,
    borders: borders || allBd(),
    margins: { top: topPad, bottom: botPad, left: 150, right: 150 },
    children: [new Paragraph({
      alignment: align,
      children: [new TextRun({ text, bold, italics: italic, size, font: 'Arial', color: color || C.ink })]
    })]
  });
}

// ─── Paragraph helpers ────────────────────────────────────────────────────
function h1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 400, after: 160 },
    children: [new TextRun({ text, bold: true, size: 38, font: 'Arial', color: C.navy })]
  });
}
function h2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 300, after: 120 },
    children: [new TextRun({ text, bold: true, size: 28, font: 'Arial', color: C.navy })]
  });
}
function h3(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_3,
    spacing: { before: 200, after: 80 },
    children: [new TextRun({ text, bold: true, size: 24, font: 'Arial', color: C.gold })]
  });
}
function p(runs, spacing={ before: 60, after: 100 }) {
  if (typeof runs === 'string') runs = [{ text: runs }];
  return new Paragraph({
    spacing,
    children: runs.map(r => new TextRun({ font: 'Arial', size: 20, color: C.ink, ...r }))
  });
}
function bullet(text, sub=false) {
  return new Paragraph({
    numbering: { reference: 'bullets', level: sub ? 1 : 0 },
    spacing: { before: 40, after: 40 },
    children: [new TextRun({ text, font: 'Arial', size: 20, color: C.ink })]
  });
}
function numbered(text) {
  return new Paragraph({
    numbering: { reference: 'numbers', level: 0 },
    spacing: { before: 40, after: 40 },
    children: [new TextRun({ text, font: 'Arial', size: 20, color: C.ink })]
  });
}
function spacer(n=1) {
  return new Paragraph({ spacing: { before: n * 80, after: 0 }, children: [] });
}
function pageBreak() {
  return new Paragraph({ children: [new PageBreak()] });
}
function divider(color=C.gold, sz=8) {
  return new Paragraph({
    spacing: { before: 120, after: 120 },
    border: { bottom: { style: BorderStyle.SINGLE, size: sz, color, space: 1 } },
    children: []
  });
}
function thinDivider() { return divider('DDDDDD', 4); }

// ─── Table builder ─────────────────────────────────────────────────────────
function makeTable(headers, rows, colWidths, hBg=C.navy, hColor=C.white) {
  const hRow = new TableRow({
    tableHeader: true,
    children: headers.map((h, i) => cell(h, {
      w: colWidths[i], bold: true, bg: hBg, color: hColor,
      align: AlignmentType.CENTER, size: 19, borders: allBd(hBg, 6)
    }))
  });
  const dRows = rows.map((row, ri) => new TableRow({
    children: row.map((val, ci) => cell(String(val), {
      w: colWidths[ci],
      bg: ri % 2 === 0 ? C.white : C.silver,
      borders: allBd('CCCCCC', 3),
      size: 19
    }))
  }));
  return new Table({
    width: { size: colWidths.reduce((a, b) => a + b, 0), type: WidthType.DXA },
    columnWidths: colWidths,
    rows: [hRow, ...dRows]
  });
}

// ─── Highlight box (2-col table trick) ────────────────────────────────────
function infoBox(label, text, bg=C.lightBlue, labelColor=C.navy) {
  const totalW = 8500;
  return new Table({
    width: { size: totalW, type: WidthType.DXA },
    columnWidths: [totalW],
    rows: [new TableRow({ children: [
      new TableCell({
        width: { size: totalW, type: WidthType.DXA },
        shading: { fill: bg, type: ShadingType.CLEAR },
        borders: { top: bd(labelColor, 8), bottom: bd('CCCCCC', 4), left: { style: BorderStyle.SINGLE, size: 20, color: labelColor }, right: bd('CCCCCC', 4) },
        margins: { top: 120, bottom: 120, left: 200, right: 200 },
        children: [
          new Paragraph({ spacing: { before: 0, after: 60 }, children: [new TextRun({ text: label, bold: true, size: 20, font: 'Arial', color: labelColor })] }),
          new Paragraph({ spacing: { before: 0, after: 0 }, children: [new TextRun({ text, size: 20, font: 'Arial', color: C.ink })] }),
        ]
      })
    ]})]
  });
}

// ─── Service block ────────────────────────────────────────────────────────
function serviceBlock(num, title, price, deliverables, timeline, requirements, color=C.navy) {
  const items = [];
  const totalW = 8500;

  // Title bar
  items.push(new Table({
    width: { size: totalW, type: WidthType.DXA },
    columnWidths: [totalW],
    rows: [new TableRow({ children: [new TableCell({
      width: { size: totalW, type: WidthType.DXA },
      shading: { fill: color, type: ShadingType.CLEAR },
      borders: allBd(color, 6),
      margins: { top: 140, bottom: 140, left: 200, right: 200 },
      children: [new Paragraph({
        alignment: AlignmentType.LEFT,
        children: [
          new TextRun({ text: `SERVICE ${num}  |  `, bold: true, size: 22, font: 'Arial', color: C.gold }),
          new TextRun({ text: title.toUpperCase(), bold: true, size: 22, font: 'Arial', color: C.white }),
          new TextRun({ text: `\t${price}`, bold: true, size: 22, font: 'Arial', color: C.gold }),
        ],
        tabStops: [{ type: TabStopType.RIGHT, position: TabStopPosition.MAX }]
      })]
    })]})],
  }));
  items.push(spacer(1));

  // 3-col meta row
  const metaW = [2200, 3100, 3200];
  items.push(new Table({
    width: { size: totalW, type: WidthType.DXA },
    columnWidths: metaW,
    rows: [
      new TableRow({ children: [
        cell('Timeline', { w: metaW[0], bold: true, bg: C.silver, color: C.navy, align: AlignmentType.CENTER, borders: allBd('CCCCCC', 4), size: 18 }),
        cell('Requirements Needed From Client', { w: metaW[1], bold: true, bg: C.silver, color: C.navy, align: AlignmentType.CENTER, borders: allBd('CCCCCC', 4), size: 18 }),
        cell('Key Deliverables', { w: metaW[2], bold: true, bg: C.silver, color: C.navy, align: AlignmentType.CENTER, borders: allBd('CCCCCC', 4), size: 18 }),
      ]},
      new TableRow({ children: [
        new TableCell({ width: { size: metaW[0], type: WidthType.DXA }, borders: allBd('CCCCCC', 3), margins: { top: 120, bottom: 120, left: 150, right: 150 },
          children: timeline.map(t => new Paragraph({ spacing: { before: 30, after: 30 }, children: [new TextRun({ text: `• ${t}`, size: 19, font: 'Arial', color: C.ink })] })) }),
        new TableCell({ width: { size: metaW[1], type: WidthType.DXA }, borders: allBd('CCCCCC', 3), margins: { top: 120, bottom: 120, left: 150, right: 150 },
          children: requirements.map(r => new Paragraph({ spacing: { before: 30, after: 30 }, children: [new TextRun({ text: `• ${r}`, size: 19, font: 'Arial', color: C.ink })] })) }),
        new TableCell({ width: { size: metaW[2], type: WidthType.DXA }, borders: allBd('CCCCCC', 3), margins: { top: 120, bottom: 120, left: 150, right: 150 },
          children: deliverables.map(d => new Paragraph({ spacing: { before: 30, after: 30 }, children: [new TextRun({ text: `• ${d}`, size: 19, font: 'Arial', color: C.ink })] })) }),
      ]})
    ]
  }));
  items.push(spacer(1));
  return items;
}

// ══════════════════════════════════════════════════════════════════════════
// BUILD DOCUMENT
// ══════════════════════════════════════════════════════════════════════════
const children = [];

// ─── COVER PAGE ──────────────────────────────────────────────────────────
children.push(spacer(5));
children.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 0, after: 60 },
  children: [new TextRun({ text: 'QUANT MARKETING AGENCY', bold: true, size: 26, font: 'Arial', color: C.gray })] }));
children.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 0, after: 40 },
  children: [new TextRun({ text: '────────────────────────────────────────', size: 22, font: 'Arial', color: C.gold })] }));
children.push(spacer(1));
children.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 0, after: 60 },
  children: [new TextRun({ text: 'SERVICE PROPOSAL', bold: true, size: 60, font: 'Arial', color: C.navy })] }));
children.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 0, after: 40 },
  children: [new TextRun({ text: 'E-Commerce Growth & Dropshipping Operations', bold: false, size: 30, font: 'Arial', color: C.gold })] }));
children.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 0, after: 40 },
  children: [new TextRun({ text: 'Saudi Arabia (KSA) Market', bold: false, size: 24, font: 'Arial', color: C.teal })] }));
children.push(spacer(2));
children.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 0, after: 40 },
  children: [new TextRun({ text: '────────────────────────────────────────', size: 22, font: 'Arial', color: C.gold })] }));
children.push(spacer(1));
// Proposal meta block
const coverW = [2600, 5000];
children.push(new Table({
  width: { size: 7600, type: WidthType.DXA },
  columnWidths: coverW,
  rows: [
    new TableRow({ children: [
      cell('Prepared For:', { w: coverW[0], bold: true, bg: C.navy, color: C.white, borders: allBd(C.navy, 4), size: 20 }),
      cell('[Client Name] / [Company Name]', { w: coverW[1], bg: C.silver, borders: allBd('CCCCCC', 3), size: 20 }),
    ]}),
    new TableRow({ children: [
      cell('Prepared By:', { w: coverW[0], bold: true, bg: C.navy, color: C.white, borders: allBd(C.navy, 4), size: 20 }),
      cell('Quant Marketing Agency', { w: coverW[1], bg: C.white, borders: allBd('CCCCCC', 3), size: 20 }),
    ]}),
    new TableRow({ children: [
      cell('Target Market:', { w: coverW[0], bold: true, bg: C.navy, color: C.white, borders: allBd(C.navy, 4), size: 20 }),
      cell('Saudi Arabia (KSA)', { w: coverW[1], bg: C.silver, borders: allBd('CCCCCC', 3), size: 20 }),
    ]}),
    new TableRow({ children: [
      cell('Proposal Date:', { w: coverW[0], bold: true, bg: C.navy, color: C.white, borders: allBd(C.navy, 4), size: 20 }),
      cell('May 2026', { w: coverW[1], bg: C.white, borders: allBd('CCCCCC', 3), size: 20 }),
    ]}),
    new TableRow({ children: [
      cell('Contract Type:', { w: coverW[0], bold: true, bg: C.navy, color: C.white, borders: allBd(C.navy, 4), size: 20 }),
      cell('Ongoing Monthly Retainer', { w: coverW[1], bg: C.silver, borders: allBd('CCCCCC', 3), size: 20 }),
    ]}),
    new TableRow({ children: [
      cell('Monthly Investment:', { w: coverW[0], bold: true, bg: C.gold, color: C.white, borders: allBd(C.gold, 4), size: 20 }),
      cell('PKR 80,000 / month', { w: coverW[1], bold: true, bg: C.lightGold, borders: allBd(C.gold, 4), size: 20 }),
    ]}),
    new TableRow({ children: [
      cell('Payment Terms:', { w: coverW[0], bold: true, bg: C.navy, color: C.white, borders: allBd(C.navy, 4), size: 20 }),
      cell('50% Advance + 50% upon milestone delivery', { w: coverW[1], bg: C.white, borders: allBd('CCCCCC', 3), size: 20 }),
    ]}),
  ]
}));
children.push(spacer(3));
children.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 0, after: 0 },
  children: [new TextRun({ text: 'Confidential & Proprietary  |  Not for Distribution', size: 18, font: 'Arial', color: C.gray, italics: true })] }));
children.push(pageBreak());

// ─── TABLE OF CONTENTS ───────────────────────────────────────────────────
children.push(h1('TABLE OF CONTENTS'));
children.push(divider());
const tocItems = [
  ['01', 'About Quant Marketing Agency', '3'],
  ['02', 'Understanding Your Business Goals', '3'],
  ['03', 'Scope of Services', '4'],
  ['    Service 1', 'Meta Ads Management', '4'],
  ['    Service 2', 'Shopify Store Development & Management', '5'],
  ['    Service 3', 'Social Media Account Management', '6'],
  ['    Service 4', 'Ads Creative Production', '7'],
  ['    Service 5', 'Analytics Integration & Reporting', '8'],
  ['04', 'Pricing Breakdown', '9'],
  ['05', 'Payment Terms & Schedule', '9'],
  ['06', 'Project Timelines & Milestones', '10'],
  ['07', 'What We Need From You (Client Requirements)', '10'],
  ['08', 'KPIs & Success Metrics', '11'],
  ['09', 'Terms & Conditions', '11'],
  ['10', 'Next Steps', '12'],
];
tocItems.forEach(([num, title, page]) => {
  const isMain = !num.startsWith('    ');
  children.push(new Paragraph({
    spacing: { before: isMain ? 80 : 40, after: 0 },
    tabStops: [{ type: TabStopType.RIGHT, position: TabStopPosition.MAX }],
    children: [
      new TextRun({ text: `${num}  ${title}`, bold: isMain, size: isMain ? 21 : 19, font: 'Arial', color: isMain ? C.navy : C.darkGray }),
      new TextRun({ text: `\t${page}`, bold: false, size: 19, font: 'Arial', color: C.gray }),
    ]
  }));
});
children.push(pageBreak());

// ─── SECTION 1: ABOUT ────────────────────────────────────────────────────
children.push(h1('01. ABOUT QUANT MARKETING AGENCY'));
children.push(divider());
children.push(p('Quant Marketing Agency is a performance-first digital growth consultancy specialising in GCC e-commerce, dropshipping operations, and paid media for brands targeting the Saudi Arabian and UAE markets. We combine data-driven strategy with creative execution to help our clients build profitable, scalable online businesses.'));
children.push(spacer(1));
const aboutW = [2100, 2100, 2100, 2200];
children.push(makeTable(
  ['Specialisation', 'Platform Expertise', 'Market Focus', 'Operating Since'],
  [['GCC Dropshipping & DTC', 'Meta · TikTok · Google', 'Saudi Arabia · UAE', '2021']],
  aboutW, C.navy, C.white
));
children.push(spacer(1));
children.push(h3('Our Core Strengths'));
children.push(bullet('End-to-end e-commerce setup — from store creation to first profitable sale'));
children.push(bullet('Deep expertise in KSA consumer psychology, Arabic creatives, and Ramadan marketing'));
children.push(bullet('Proven COD order management systems reducing return rates below 15%'));
children.push(bullet('In-house creative team producing high-converting UGC and studio-quality ad content'));
children.push(bullet('Full analytics stack integration — Meta Pixel, GA4, server-side tracking, Klaviyo'));
children.push(pageBreak());

// ─── SECTION 2: UNDERSTANDING YOUR GOALS ─────────────────────────────────
children.push(h1('02. UNDERSTANDING YOUR BUSINESS GOALS'));
children.push(divider());
children.push(p('Based on our initial consultation and the market research provided, we understand your primary objectives are:'));
children.push(spacer(1));
children.push(infoBox('Primary Goal',
  'Launch and scale a profitable dropshipping business targeting the Saudi Arabian (KSA) market, using KSA-based local suppliers, with a focus on high-margin product categories (Home & Kitchen, Personal Care, Baby Products) and paid social advertising as the primary customer acquisition channel.',
  C.lightBlue, C.teal));
children.push(spacer(1));
children.push(makeTable(
  ['Your Goal', 'Our Solution'],
  [
    ['Launch a KSA-ready Shopify store', 'Full store build — Arabic/English, COD, MADA, Tamara'],
    ['Drive sales via paid ads (Meta + TikTok)', 'Full Meta Ads management + creative production'],
    ['Build brand presence on social media', 'Social media account management (Arabic-first)'],
    ['Make data-informed decisions', 'Full analytics integration — GA4, Meta Pixel, dashboards'],
    ['Minimise COD return rate', 'Pre-order confirmation SOP + courier optimisation'],
    ['Scale profitably month-over-month', 'Monthly retainer model with full performance reporting'],
  ],
  [3800, 4700], C.navy
));
children.push(pageBreak());

// ─── SECTION 3: SCOPE OF SERVICES ────────────────────────────────────────
children.push(h1('03. SCOPE OF SERVICES'));
children.push(divider());
children.push(p([{text:'This proposal covers five integrated services, ',bold:false},{text:'each essential to launching and scaling a profitable KSA dropshipping operation.',bold:true}]));
children.push(spacer(1));

// ── SERVICE 1: META ADS ──────────────────────────────────────────────────
const svc1 = serviceBlock(
  '01', 'Meta Ads Management', 'PKR 20,000 / month',
  [
    'Full campaign setup (cold + warm + retargeting)',
    'Ad set structure (ABO + CBO)',
    'Audience research & segmentation',
    'Weekly performance reports',
    'A/B testing (creative, copy, audience)',
    'ROAS & CPA optimisation',
    'Pixel troubleshooting & event verification',
    'Scaling strategy (LAL, broad, retargeting)',
    'Monthly strategy review call',
  ],
  [
    'Setup: 5–7 business days',
    'First results: Day 3–7',
    'Optimisation cycle: Every 3 days',
    'Full scaling: Day 30–45',
    'Reports: Weekly + monthly',
  ],
  [
    'Active Facebook Business Manager',
    'Facebook Page (KSA-focused)',
    'Meta Pixel installed on store',
    'Ad account with billing method',
    'Ad spend budget (separate from fee)',
    'Product images / videos for ads',
    'WhatsApp or email for daily comms',
  ]
);
svc1.forEach(i => children.push(i));

// ── SERVICE 2: SHOPIFY ───────────────────────────────────────────────────
const svc2 = serviceBlock(
  '02', 'Shopify Store Development & Management', 'PKR 20,000 / month',
  [
    'Full store build (Arabic + English)',
    'RTL (Right-to-Left) text support',
    'Mobile-first responsive design',
    'Product listing with Arabic copy',
    'MADA + COD + Tamara payment setup',
    'Moyasar / Telr gateway integration',
    'Shipping zones & COD configuration',
    'Upsell & cross-sell apps setup',
    'Abandoned cart recovery automation',
    'Monthly product additions (up to 10)',
    'Ongoing store maintenance & updates',
  ],
  [
    'Initial build: 10–14 business days',
    'Revisions: 3–5 business days',
    'Go-live: Day 14–18',
    'Monthly maintenance: Ongoing',
    'New product adds: Within 48 hrs',
  ],
  [
    'Shopify plan (Basic or above)',
    'Domain name (if available)',
    'Brand logo & brand colours',
    'Product sourcing confirmed (Ritad / CJD)',
    'Supplier product images & descriptions',
    'Preferred store name & tagline',
    'Moyasar / Telr merchant account',
  ]
);
svc2.forEach(i => children.push(i));

children.push(pageBreak());

// ── SERVICE 3: SOCIAL MEDIA MANAGEMENT ──────────────────────────────────
const svc3 = serviceBlock(
  '03', 'Social Media Account Management', 'PKR 15,000 / month',
  [
    'Instagram & TikTok account setup/optimisation',
    '12 posts/month (feed + reels)',
    'Arabic-first captions & hashtag research',
    'Story content (3x per week)',
    'Community management (DM replies)',
    'Competitor analysis (monthly)',
    'Content calendar planning',
    'KSA-relevant trending content integration',
    'Ramadan & seasonal campaign content',
    'Monthly analytics report (reach, engagement)',
  ],
  [
    'Account audit & setup: 3–5 days',
    'First content calendar: Day 5–7',
    'First post goes live: Day 7',
    'Ongoing: 12 posts/month',
    'Monthly report: End of each month',
  ],
  [
    'Instagram & TikTok login credentials',
    'Brand guidelines (colours, fonts, tone)',
    'Product photos or raw footage',
    'Approval for content calendar monthly',
    'Feedback within 24 hrs on drafts',
    'Any upcoming promotions / offers info',
  ]
);
svc3.forEach(i => children.push(i));

// ── SERVICE 4: ADS CREATIVE PRODUCTION ───────────────────────────────────
const svc4 = serviceBlock(
  '04', 'Ads Creative Production', 'PKR 15,000 / month',
  [
    '4 video ad creatives/month (30–45 sec each)',
    '6 static image ads/month',
    'Arabic voiceover on all video ads',
    'Subtitles (Arabic + English)',
    'Hook testing variants (3 hooks/video)',
    'TikTok-format & Meta-format versions',
    'UGC-style scripting & direction notes',
    'Product demo & before/after formats',
    'Seasonal creative (Ramadan, Eid, etc.)',
    'Ad copy (headline + primary + CTA)',
  ],
  [
    'Brief & scripting: Days 1–3',
    'Production: Days 3–7',
    'Review & revisions: Days 7–10',
    'Final delivery: Day 10–12',
    'Monthly cycle resets each month',
  ],
  [
    'Product sample / unboxing footage (or we source)',
    'Brand logo in high resolution (PNG)',
    'Preferred colour scheme',
    'Any existing customer testimonials',
    'List of key product benefits (in any language)',
    'Approval turnaround within 48 hrs',
  ]
);
svc4.forEach(i => children.push(i));

children.push(pageBreak());

// ── SERVICE 5: ANALYTICS INTEGRATION ────────────────────────────────────
const svc5 = serviceBlock(
  '05', 'Analytics Integration & Reporting', 'PKR 10,000 / month',
  [
    'Meta Pixel full setup + event verification',
    'Google Analytics 4 (GA4) integration',
    'Shopify — GA4 e-commerce tracking',
    'Server-side tracking (via Stape.io)',
    'Conversion API (CAPI) setup',
    'Custom KPI dashboard (Looker Studio)',
    'UTM parameter framework',
    'COD order tracking & return rate reports',
    'Monthly analytics report (PDF)',
    'Ad spend vs. revenue reconciliation',
  ],
  [
    'Initial setup: 5–7 business days',
    'Dashboard live: Day 7–10',
    'First report: End of Month 1',
    'Ongoing: Monthly reports',
    'Data audit: Quarterly',
  ],
  [
    'Shopify admin access (staff account)',
    'Google account for GA4 property',
    'Facebook Business Manager access',
    'Domain access for pixel verification',
    'Stape.io account (or we set up)',
    'Preferred KPI metrics to track',
  ]
);
svc5.forEach(i => children.push(i));

// ─── SECTION 4: PRICING BREAKDOWN ────────────────────────────────────────
children.push(h1('04. PRICING BREAKDOWN'));
children.push(divider());
children.push(p('All prices are in Pakistani Rupees (PKR). Ad spend budgets are separate and paid directly to Meta/TikTok by the client.'));
children.push(spacer(1));

const priceHdr = new TableRow({ tableHeader: true, children: [
  cell('Service', { w:4500, bold:true, bg:C.navy, color:C.white, borders:allBd(C.navy,6), size:20 }),
  cell('Description', { w:2500, bold:true, bg:C.navy, color:C.white, align:AlignmentType.CENTER, borders:allBd(C.navy,6), size:20 }),
  cell('Monthly Fee (PKR)', { w:2000, bold:true, bg:C.navy, color:C.white, align:AlignmentType.CENTER, borders:allBd(C.navy,6), size:20 }),
]});
const priceRows = [
  ['Meta Ads Management', 'Campaign strategy, setup, optimisation & scaling', 'PKR 20,000'],
  ['Shopify Store Development & Management', 'Store build, Arabic/English, products, maintenance', 'PKR 20,000'],
  ['Social Media Account Management', 'Instagram & TikTok — 12 posts/month, community mgmt', 'PKR 15,000'],
  ['Ads Creative Production', '4 video ads + 6 static ads with Arabic VO & copy', 'PKR 15,000'],
  ['Analytics Integration & Reporting', 'Pixel, GA4, CAPI, dashboard & monthly reports', 'PKR 10,000'],
].map((row, ri) => new TableRow({ children: [
  cell(row[0], { w:4500, bold:false, bg: ri%2===0?C.white:C.silver, borders:allBd('CCCCCC',3), size:19 }),
  cell(row[1], { w:2500, bold:false, bg: ri%2===0?C.white:C.silver, borders:allBd('CCCCCC',3), size:19 }),
  cell(row[2], { w:2000, bold:false, bg: ri%2===0?C.white:C.silver, align:AlignmentType.CENTER, borders:allBd('CCCCCC',3), size:19 }),
]}));
const totalRow = new TableRow({ children: [
  cell('TOTAL MONTHLY RETAINER', { w:4500, bold:true, bg:C.gold, color:C.white, borders:allBd(C.gold,6), size:21 }),
  cell('All 5 services included', { w:2500, bold:true, bg:C.gold, color:C.white, align:AlignmentType.CENTER, borders:allBd(C.gold,6), size:21 }),
  cell('PKR 80,000', { w:2000, bold:true, bg:C.green, color:C.white, align:AlignmentType.CENTER, borders:allBd(C.green,6), size:21 }),
]});
const advanceRow = new TableRow({ children: [
  cell('50% Advance (Due Before Work Begins)', { w:4500, bold:true, bg:C.lightGold, borders:allBd(C.gold,4), size:20 }),
  cell('Required to initiate all services', { w:2500, bold:false, bg:C.lightGold, align:AlignmentType.CENTER, borders:allBd(C.gold,4), size:19 }),
  cell('PKR 40,000', { w:2000, bold:true, bg:C.lightGold, align:AlignmentType.CENTER, borders:allBd(C.gold,4), size:20 }),
]});
const balanceRow = new TableRow({ children: [
  cell('50% Balance (Due on Milestone Delivery)', { w:4500, bold:true, bg:C.silver, borders:allBd('CCCCCC',4), size:20 }),
  cell('Upon store go-live or agreed milestone', { w:2500, bold:false, bg:C.silver, align:AlignmentType.CENTER, borders:allBd('CCCCCC',4), size:19 }),
  cell('PKR 40,000', { w:2000, bold:true, bg:C.silver, align:AlignmentType.CENTER, borders:allBd('CCCCCC',4), size:20 }),
]});

children.push(new Table({
  width: { size: 9000, type: WidthType.DXA },
  columnWidths: [4500, 2500, 2000],
  rows: [priceHdr, ...priceRows, totalRow, advanceRow, balanceRow]
}));
children.push(spacer(1));
children.push(infoBox('Important Note on Ad Spend',
  'The monthly fee of PKR 80,000 covers agency services ONLY. Meta and TikTok ad spend budgets are paid directly by the client to the respective platforms and are NOT included in this fee. We recommend a minimum ad spend of PKR 50,000–80,000/month for meaningful KSA results.',
  C.lightGold, C.gold));
children.push(pageBreak());

// ─── SECTION 5: PAYMENT TERMS ────────────────────────────────────────────
children.push(h1('05. PAYMENT TERMS & SCHEDULE'));
children.push(divider());
children.push(makeTable(
  ['Term', 'Details'],
  [
    ['Payment Structure', '50% advance + 50% upon milestone delivery — every month'],
    ['Advance Payment', 'PKR 40,000 — due before any work begins each month'],
    ['Balance Payment', 'PKR 40,000 — due upon store go-live (Month 1) or on agreed monthly milestone'],
    ['Payment Method', 'Bank transfer (account details shared upon agreement)'],
    ['Invoice Frequency', 'Monthly invoice issued on the 1st of each month'],
    ['Late Payment Policy', 'Work pauses if balance not received within 5 business days of milestone'],
    ['Currency', 'Pakistani Rupees (PKR) only'],
    ['Contract Notice Period', '15 days written notice required to cancel or pause services'],
    ['Refund Policy', 'Advance is non-refundable once work has commenced on that service'],
  ],
  [3500, 5000], C.navy
));
children.push(spacer(1));
children.push(h3('Monthly Payment Flow'));
children.push(makeTable(
  ['Step', 'Action', 'Amount', 'Timing'],
  [
    ['1', 'Client pays advance — services begin', 'PKR 40,000', '1st of each month (or project start)'],
    ['2', 'Agency delivers agreed milestone', '—', 'As per timeline in each service scope'],
    ['3', 'Client pays balance — next cycle begins', 'PKR 40,000', 'Within 5 days of milestone delivery'],
    ['4', 'Monthly report issued', '—', 'Last business day of month'],
  ],
  [400, 3200, 1600, 3300], C.teal
));
children.push(pageBreak());

// ─── SECTION 6: TIMELINES & MILESTONES ───────────────────────────────────
children.push(h1('06. PROJECT TIMELINES & MILESTONES'));
children.push(divider());
children.push(p('All timelines begin from the date advance payment is confirmed and all client requirements are received.'));
children.push(spacer(1));
children.push(makeTable(
  ['Week', 'Milestone', 'Services Active', 'Client Action Required'],
  [
    ['Week 1 (Days 1–7)', 'Advance received · Onboarding call · Brief collection', 'All 5', 'Provide all access & assets'],
    ['Week 1–2 (Days 5–14)', 'Shopify store in development · Analytics being set up · Social accounts audited', 'Shopify, Analytics, Social', 'Review draft store design'],
    ['Week 2 (Days 7–12)', 'First ad creatives produced · Meta Pixel installed', 'Creative, Analytics', 'Approve creatives within 48 hrs'],
    ['Week 2–3 (Days 14–18)', 'Store go-live · Payment gateways live · COD enabled', 'Shopify', 'Confirm store approval & go-live'],
    ['Week 3 (Days 14–18)', 'Meta Ads campaigns launched · First ad sets live', 'Meta Ads', 'Approve campaigns & ad spend'],
    ['Week 3 (Days 15–18)', 'Social media first posts · Content calendar shared', 'Social Media', 'Approve content calendar'],
    ['Week 3–4 (Days 18–21)', 'Analytics dashboard live · GA4 tracking verified', 'Analytics', 'Review dashboard & confirm KPIs'],
    ['End of Month 1', 'First monthly performance report delivered', 'All 5', 'Review report · Pay Month 2 advance'],
    ['Month 2+', 'Ongoing: Optimisation, scaling, content, reporting', 'All 5', 'Monthly approval & payment cycle'],
  ],
  [1500, 2700, 2400, 2400], C.navy
));
children.push(spacer(1));
children.push(infoBox('Timeline Dependency Notice',
  'All timelines above are contingent on the client providing required assets, access credentials, and approvals within the timeframes specified. Any delays in client-side deliverables will extend the project timeline by an equivalent number of business days.',
  C.lightBlue, C.teal));
children.push(pageBreak());

// ─── SECTION 7: CLIENT REQUIREMENTS ──────────────────────────────────────
children.push(h1('07. WHAT WE NEED FROM YOU'));
children.push(divider());
children.push(p('To begin work immediately upon advance payment, please prepare and share the following:'));
children.push(spacer(1));
children.push(makeTable(
  ['Item Required', 'Purpose', 'Format', 'Urgency'],
  [
    ['Facebook Business Manager access', 'Meta Ads setup & Pixel install', 'Admin/Analyst role invite', 'Day 1'],
    ['Facebook Page credentials', 'Ads management', 'Page admin access', 'Day 1'],
    ['Shopify login or new account', 'Store development', 'Staff account or owner creds', 'Day 1'],
    ['Domain name (if purchased)', 'Store URL setup', 'Domain + DNS access', 'Day 1'],
    ['Brand logo (high resolution)', 'Store + creatives + social', 'PNG, transparent background', 'Day 1'],
    ['Brand colours & style guide', 'Design consistency', 'Hex codes or reference images', 'Day 1'],
    ['Google account (for GA4)', 'Analytics integration', 'Gmail or Workspace account', 'Day 1'],
    ['Instagram + TikTok credentials', 'Social media management', 'Username & password or collab access', 'Day 2'],
    ['Product supplier confirmation', 'Listings & ad angles', 'Ritad / CJD products selected', 'Day 2'],
    ['Product images/videos (if available)', 'Ad creatives & listings', 'JPG/PNG/MP4 (high quality)', 'Day 2–3'],
    ['Moyasar or Telr merchant account', 'Payment gateway (KSA)', 'Account access or we assist setup', 'Day 3–5'],
    ['Preferred store name & tagline', 'Branding', 'In English + Arabic (if available)', 'Day 1'],
    ['WhatsApp / communication channel', 'Daily coordination', 'WhatsApp number or email', 'Day 1'],
  ],
  [2800, 2000, 1800, 1400], C.navy
));
children.push(pageBreak());

// ─── SECTION 8: KPIs & SUCCESS METRICS ───────────────────────────────────
children.push(h1('08. KPIs & SUCCESS METRICS'));
children.push(divider());
children.push(p('We measure success through the following KPIs, tracked monthly and reported in your performance dashboard:'));
children.push(spacer(1));
children.push(makeTable(
  ['KPI', 'Target (Month 1)', 'Target (Month 3)', 'Target (Month 6)'],
  [
    ['Blended ROAS (Return on Ad Spend)', '2.0–2.5x', '3.0–4.0x', '4.0–5.5x'],
    ['Monthly Revenue (SAR)', 'SAR 15,000–30,000', 'SAR 60,000–100,000', 'SAR 150,000–250,000'],
    ['COD Return-to-Origin Rate', '< 25%', '< 20%', '< 15%'],
    ['Cost Per Purchase (CPA)', 'SAR 60–90', 'SAR 40–65', 'SAR 30–50'],
    ['Store Conversion Rate', '1.5–2.0%', '2.5–3.5%', '3.0–4.5%'],
    ['Meta Ads CTR (Cold Traffic)', '1.5–2.0%', '2.0–3.0%', '2.5–3.5%'],
    ['Social Media Followers Growth', '+300–500/mo', '+800–1,500/mo', '+2,000–3,500/mo'],
    ['Engagement Rate (Social)', '2–4%', '4–6%', '5–8%'],
    ['Meta Pixel Match Rate', '> 70%', '> 80%', '> 85%'],
    ['Email/WhatsApp List Growth', '+100–200/mo', '+400–700/mo', '+1,000–1,500/mo'],
  ],
  [3000, 2000, 2000, 2000], C.navy
));
children.push(spacer(1));
children.push(p([{text:'Reporting Cadence: ',bold:true},{text:'Weekly performance snapshots (Meta Ads metrics) + end-of-month comprehensive PDF report covering all 5 service areas. Monthly strategy review call included.'}]));
children.push(pageBreak());

// ─── SECTION 9: TERMS & CONDITIONS ───────────────────────────────────────
children.push(h1('09. TERMS & CONDITIONS'));
children.push(divider());

children.push(h3('1. Engagement & Commencement'));
children.push(bullet('Work commences upon receipt of the 50% advance payment (PKR 40,000) and signed acceptance of this proposal.'));
children.push(bullet('The retainer renews automatically on a monthly basis unless written notice is provided.'));

children.push(h3('2. Payment & Invoicing'));
children.push(bullet('All fees are payable in PKR via bank transfer.'));
children.push(bullet('The 50% advance is due on the 1st of each retainer month (or project commencement date).'));
children.push(bullet('The 50% balance is due within 5 business days of milestone/go-live delivery.'));
children.push(bullet('Late payments beyond 5 business days will result in work being paused until payment is cleared.'));
children.push(bullet('The advance payment is non-refundable once work on that month has commenced.'));

children.push(h3('3. Client Responsibilities'));
children.push(bullet('The client agrees to provide all required assets, access credentials, and approvals within the timeframes specified in Section 07.'));
children.push(bullet('Delays caused by late provision of client materials will extend timelines by an equivalent number of business days, with no penalty to the agency.'));
children.push(bullet('The client is responsible for all third-party costs including Shopify subscription, domain, ad spend, payment gateway fees, and app subscriptions.'));

children.push(h3('4. Intellectual Property'));
children.push(bullet('All creative assets (ad videos, static images, copy) produced by Quant Marketing Agency become the property of the client upon full payment of that month\'s fees.'));
children.push(bullet('The agency retains the right to showcase the work in its portfolio unless the client requests otherwise in writing.'));

children.push(h3('5. Confidentiality'));
children.push(bullet('Both parties agree to keep all business information, strategies, login credentials, and financial data strictly confidential.'));

children.push(h3('6. Performance & Guarantees'));
children.push(bullet('Quant Marketing Agency does not guarantee specific revenue figures or ROAS outcomes, as performance is subject to market conditions, ad spend levels, product quality, and client-side factors.'));
children.push(bullet('The KPI targets in Section 08 are data-informed benchmarks, not contractual guarantees.'));
children.push(bullet('The agency commits to best-practice management, transparent reporting, and proactive optimisation at all times.'));

children.push(h3('7. Termination & Notice'));
children.push(bullet('Either party may terminate the retainer with 15 days written notice (WhatsApp or email).'));
children.push(bullet('Upon termination, the agency will deliver all completed work, creative files, and data to the client within 5 business days.'));
children.push(bullet('No partial refunds are issued for the month in which notice is given if work has commenced.'));

children.push(h3('8. Amendments'));
children.push(bullet('Any changes to the scope of services must be agreed in writing and may be subject to additional fees.'));
children.push(pageBreak());

// ─── SECTION 10: NEXT STEPS ───────────────────────────────────────────────
children.push(h1('10. NEXT STEPS'));
children.push(divider());
children.push(p('To move forward and begin your KSA dropshipping journey with Quant Marketing Agency, simply follow these steps:'));
children.push(spacer(1));
children.push(makeTable(
  ['Step', 'Action', 'Responsible', 'Timeline'],
  [
    ['1', 'Review this proposal and confirm acceptance via WhatsApp or email', 'Client', 'Within 2–3 days'],
    ['2', 'Quant sends bank account details for advance payment', 'Quant Marketing Agency', 'Same day'],
    ['3', 'Client transfers PKR 40,000 advance payment', 'Client', 'Within 24 hrs of confirmation'],
    ['4', 'Onboarding call scheduled (30–45 minutes)', 'Both Parties', 'Day 1 of engagement'],
    ['5', 'Client provides all assets & access (per Section 07)', 'Client', 'Days 1–3'],
    ['6', 'Work commences across all 5 services simultaneously', 'Quant Marketing Agency', 'Day 1–2 after receipt of assets'],
    ['7', 'Store go-live + first ads launch', 'Quant Marketing Agency', 'Days 14–18'],
    ['8', 'First weekly performance update shared', 'Quant Marketing Agency', 'Day 7 of engagement'],
  ],
  [400, 3500, 2200, 2400], C.navy
));
children.push(spacer(1));
children.push(infoBox('Ready to Start?',
  'Contact us on WhatsApp or email to confirm your acceptance. Once the advance payment is received, our team begins work within 24 hours. We are excited to build your KSA e-commerce success story together.',
  C.lightGreen, C.green));
children.push(spacer(2));

// Signature block
const sigW = [4250, 4250];
children.push(new Table({
  width: { size: 8500, type: WidthType.DXA },
  columnWidths: sigW,
  rows: [
    new TableRow({ children: [
      cell('Quant Marketing Agency', { w:sigW[0], bold:true, bg:C.navy, color:C.white, align:AlignmentType.CENTER, borders:allBd(C.navy,6), size:21 }),
      cell('[Client Name / Company]', { w:sigW[1], bold:true, bg:C.navy, color:C.white, align:AlignmentType.CENTER, borders:allBd(C.navy,6), size:21 }),
    ]}),
    new TableRow({ children: [
      new TableCell({ width:{size:sigW[0],type:WidthType.DXA}, borders:allBd('CCCCCC',3), margins:{top:200,bottom:200,left:150,right:150},
        children:[
          new Paragraph({spacing:{before:0,after:60},children:[new TextRun({text:'Authorised Signature:', size:18,font:'Arial',color:C.gray})]}),
          new Paragraph({spacing:{before:0,after:60},children:[new TextRun({text:'_________________________________', size:20,font:'Arial',color:C.navy})]}),
          new Paragraph({spacing:{before:0,after:60},children:[new TextRun({text:'Name: ___________________________', size:18,font:'Arial',color:C.darkGray})]}),
          new Paragraph({spacing:{before:0,after:60},children:[new TextRun({text:'Date:  ___________________________', size:18,font:'Arial',color:C.darkGray})]}),
        ]
      }),
      new TableCell({ width:{size:sigW[1],type:WidthType.DXA}, borders:allBd('CCCCCC',3), margins:{top:200,bottom:200,left:150,right:150},
        children:[
          new Paragraph({spacing:{before:0,after:60},children:[new TextRun({text:'Client Signature:', size:18,font:'Arial',color:C.gray})]}),
          new Paragraph({spacing:{before:0,after:60},children:[new TextRun({text:'_________________________________', size:20,font:'Arial',color:C.navy})]}),
          new Paragraph({spacing:{before:0,after:60},children:[new TextRun({text:'Name: ___________________________', size:18,font:'Arial',color:C.darkGray})]}),
          new Paragraph({spacing:{before:0,after:60},children:[new TextRun({text:'Date:  ___________________________', size:18,font:'Arial',color:C.darkGray})]}),
        ]
      }),
    ]}),
  ]
}));
children.push(spacer(2));
children.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing:{before:0,after:0},
  children:[new TextRun({text:'Thank you for the opportunity to partner in your growth. We look forward to building something exceptional together.',size:20,font:'Arial',color:C.navy,italics:true})]}));

// ══════════════════════════════════════════════════════════════════════════
// ASSEMBLE
// ══════════════════════════════════════════════════════════════════════════
const doc = new Document({
  numbering: {
    config: [
      { reference:'bullets', levels:[{
        level:0, format:LevelFormat.BULLET, text:'•', alignment:AlignmentType.LEFT,
        style:{ paragraph:{ indent:{ left:720, hanging:360 } } }
      },{
        level:1, format:LevelFormat.BULLET, text:'◦', alignment:AlignmentType.LEFT,
        style:{ paragraph:{ indent:{ left:1080, hanging:360 } } }
      }]},
      { reference:'numbers', levels:[{
        level:0, format:LevelFormat.DECIMAL, text:'%1.', alignment:AlignmentType.LEFT,
        style:{ paragraph:{ indent:{ left:720, hanging:360 } } }
      }]},
    ]
  },
  styles: {
    default: { document: { run:{ font:'Arial', size:20 } } },
    paragraphStyles: [
      { id:'Heading1', name:'Heading 1', basedOn:'Normal', next:'Normal', quickFormat:true,
        run:{ size:38, bold:true, font:'Arial', color:C.navy },
        paragraph:{ spacing:{ before:400, after:160 }, outlineLevel:0 } },
      { id:'Heading2', name:'Heading 2', basedOn:'Normal', next:'Normal', quickFormat:true,
        run:{ size:28, bold:true, font:'Arial', color:C.navy },
        paragraph:{ spacing:{ before:300, after:120 }, outlineLevel:1 } },
      { id:'Heading3', name:'Heading 3', basedOn:'Normal', next:'Normal', quickFormat:true,
        run:{ size:24, bold:true, font:'Arial', color:C.gold },
        paragraph:{ spacing:{ before:200, after:80 }, outlineLevel:2 } },
    ]
  },
  sections: [{
    properties: {
      page: {
        size: { width:12240, height:15840 },
        margin: { top:1080, right:1080, bottom:1080, left:1080 }
      }
    },
    headers: {
      default: new Header({ children:[
        new Paragraph({
          border:{ bottom:{ style:BorderStyle.SINGLE, size:6, color:C.gold, space:1 } },
          spacing:{ before:0, after:120 },
          tabStops:[{ type:TabStopType.RIGHT, position:TabStopPosition.MAX }],
          children:[
            new TextRun({ text:'QUANT MARKETING AGENCY', bold:true, size:16, font:'Arial', color:C.navy }),
            new TextRun({ text:'  |  Service Proposal — KSA E-Commerce', size:16, font:'Arial', color:C.gray }),
            new TextRun({ text:'\tMay 2026', size:16, font:'Arial', color:C.gray }),
          ]
        })
      ]})
    },
    footers: {
      default: new Footer({ children:[
        new Paragraph({
          border:{ top:{ style:BorderStyle.SINGLE, size:6, color:C.gold, space:1 } },
          spacing:{ before:120, after:0 },
          tabStops:[{ type:TabStopType.RIGHT, position:TabStopPosition.MAX }],
          children:[
            new TextRun({ text:'Confidential  |  Not for Distribution', size:16, font:'Arial', color:C.gray, italics:true }),
            new TextRun({ text:'\tPage ', size:16, font:'Arial', color:C.gray }),
            new TextRun({ children:[PageNumber.CURRENT], size:16, font:'Arial', color:C.gray }),
          ]
        })
      ]})
    },
    children
  }]
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync('/mnt/user-data/outputs/Quant_Agency_Service_Proposal_KSA_2026.docx', buf);
  console.log('Done');
}).catch(e => { console.error(e); process.exit(1); });