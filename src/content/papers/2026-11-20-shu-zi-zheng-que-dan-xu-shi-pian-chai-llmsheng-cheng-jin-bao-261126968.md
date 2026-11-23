---
title: 'Right Numbers, Wrong Story: When LLMs Narrate Financial Changes Beyond Their
  Inputs'
title_zh: 数字正确但叙事偏差：LLM生成金融报告的无依据表述问题及修复
authors:
- Seunghan Lee
- Jun Seo
- Junhyeok Kang
- Jaehoon Lee
- Sangjun Han
- Sungdong Yoo
- Minjae Kim
- Tae Yoon Lim
- Dongwan Kang
- Hwanil Choi
affiliations:
- LG AI Research
arxiv_id: '2611.26968'
url: https://arxiv.org/abs/2611.26968
pdf_url: https://arxiv.org/pdf/2611.26968
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: LLM生成内容合规性校验与优化
tags:
- Hallucination
- Financial NLP
- Text Correction
- Factuality
- LLM Alignment
one_liner: 提出无额外模型调用的FrameCheck插件，消除LLM金融报告无依据表述，对齐专业10-K水平
practical_value: '- 电商/营销文案生成场景可直接复用框架：先基于业务历史合规语料构建修饰词、表述规范库，生成前注入同场景Few-shot样例引导，生成后用规则过滤无依据修饰词、非输入支撑的因果表述，全程无额外模型调用，成本极低。

  - 生成类业务流程设计可复用结论：不要盲目依赖Prompt工程约束LLM不添加额外信息，论文明确显示给LLM列术语使用范围反而会让无依据判断增多，规则后处理的效果远好于单纯Prompt优化。

  - 生成内容合规校验可分层实现：无需全量上LLM Judge，先通过关键词匹配（因果连接词、业务修饰词库）做规则过滤，可解决80%以上低阶合规问题，大幅降低校验成本。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM越来越多用于生成金融报告、财报等合规性要求高的文本，现有校验仅关注数字准确性，忽略了LLM会额外添加无依据的判断修饰词（比如把增长3%写成“大幅增长3%”）和无输入支撑的因果解释，这类“无依据表述”在监管披露场景会引发合规风险，且常规Prompt优化不仅解决不了问题甚至会加剧。

### 方法关键点
- 先从22万份美国10-K财报的MD&A章节构建专业术语使用规范：统计78个量级修饰词（如slightly、sharply）的适用变化幅度区间（10%-90%分位），作为判断表述是否合规的基准。
- 三步无额外模型调用工作流：1）生成前给Prompt注入相同变化幅度的10-K专业样例做Few-shot引导；2）生成后校验：修饰词是否落在适用区间、因果表述的核心内容是否在输入中存在；3）规则编辑：直接删除不合规修饰词、无依据因果从句，替换违规动词为中性表述。

### 关键实验
在17款开源LLM、300万份生成草稿上测试，对比Prompt优化、Self-Refine、CoVe等现有后编辑工具基线：FrameCheck将含无依据因果表述的草稿占比从77%降到0.4%，判断词使用率从17.2%降到1.0%，接近专业10-K作者的1.5%水平，全程无额外模型调用，成本远低于其他后处理方案。

### 最值得记住的一句话
正确的数字不等于正确的句子，生成类业务的合规校验不能只停留在事实匹配层面，还要关注表述的规范性与输入边界的一致性。
