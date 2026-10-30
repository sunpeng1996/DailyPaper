---
title: 'InterA11y: Interactive Web Accessibility Error Detection with LLM Agents'
title_zh: InterA11y：基于LLM Agent的交互式网页无障碍错误检测系统
authors:
- Mingyuan Zhong
- Mengqi Shi
- Davin Win Kyi
- Ajit Mallavarapu
- Xia Chen
- James Fogarty
- Jacob O. Wobbrock
affiliations:
- University of Washington
- Cornell University
- Carnegie Mellon University
arxiv_id: '2610.39488'
url: https://arxiv.org/abs/2610.39488
pdf_url: https://arxiv.org/pdf/2610.39488
published: '2026-10-29'
collected: '2026-10-30'
category: Agent
direction: Agent 网页无障碍自动化检测
tags:
- LLM Agent
- Web Accessibility
- WCAG
- Interactive Tool
- Automated Testing
one_liner: 结合WCAG拆解规则与交互式工具的LLM Agent系统，大幅提升网页无障碍检测的召回与稳定性
practical_value: '- 做垂直领域合规/功能检测Agent时，可将行业标准拆解为结构化执行rubric，明确每步的证据要求与判定逻辑，大幅降低LLM幻觉，提升输出稳定性

  - 针对需要交互验证的检测场景（如电商页面功能可用性、弹窗可关闭性、键盘导航合规性），封装领域专用确定性交互工具，代替Agent盲目工具调用，既降低误报率，又减少token消耗

  - 通用Agent落地垂直场景时，注入垂直领域专用工具即可获得显著性能提升，无需重新训练基座或大规模调整Agent架构'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有基于LLM的网页无障碍检测仅依赖静态HTML、截图信息，缺少动态交互验证，召回低、误报高，且不同基座模型性能波动大，无法满足合规检测的可靠性要求；传统规则引擎覆盖的WCAG合规场景不足30%，大量需要语义理解、交互验证的场景只能靠人工审核，成本极高。
### 方法关键点
- 将10项高频违反的WCAG合规标准拆解为35条可执行评分rubric，每一条明确所需证据类型、判定逻辑、对应调用工具，引导Agent步骤化收集证据
- 封装46个交互式工具，覆盖页面信息检查、视觉属性采集、样式测量、页面交互、响应监控5大类，可确定性采集交互场景下的证据（如焦点跳转逻辑、键盘导航可用性、灰度下颜色区分度等）
- 采用两级判定流程：先通过确定性规则输出明确结果，不确定场景再由LLM基于rubric调用工具补充证据后输出判定
### 关键结果
在197个真实网页的专家标注数据集上对比三类基线（规则引擎、现有LLM检测方案、通用网页Agent）：
- InterA11y召回达79.0%，较最优LLM基线的44.4%高34.6pct，精度93.1%与最优规则引擎的90.3~97.6%持平，不同基座模型性能波动小于8%
- 给通用网页Agent注入本方案的专用工具后，召回平均提升20pct，token消耗降低14~38%
### 核心结论
垂直领域Agent的可靠性提升，核心不是换更强的基座，而是把领域知识拆解成结构化的执行规则，再配套确定性的专用工具降低证据收集的不确定性
