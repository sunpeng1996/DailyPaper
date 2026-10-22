---
title: 'What the Author Wrote, What the Agent Reads: Silent Cue Loss in Enterprise
  Document Ingestion'
title_zh: 企业文档摄入阶段的隐性格式提示丢失问题研究
authors:
- Yikai Zhao
- Saurabh Pandey
- Pradeep Kumar Misra
affiliations:
- Amazon
arxiv_id: '2610.30026'
url: https://arxiv.org/abs/2610.30026
pdf_url: https://arxiv.org/pdf/2610.30026
published: '2026-10-21'
collected: '2026-10-22'
category: Agent
direction: Agent · 企业文档格式感知解析
tags:
- Document Parsing
- Enterprise Agent
- Formatting Cue
- Information Loss
- RAG
one_liner: 量化企业文档解析中格式提示丢失对Agent的影响，定位核心影响因子并给出低成本修复方案
practical_value: '- 做企业级RAG/文档处理Agent时，优先保留高亮、颜色两类格式提示，两类贡献了全部格式相关性能收益，远大于粗体、斜体等其他格式

  - 解析docx/PDF时需显式提取页眉、页脚、脚注、修订记录等非body区域内容，现有主流转换工具都会默认丢失这部分信息

  - 提取到格式提示后不要仅输出原始标记（如`[COLOR:#FF0000]`），需附加语义类型标签（如`CRITICAL_WARNING`），可带来约8.5%的F1提升，全程无需LLM调用，成本极低

  - 监控RAG链路不能仅校验输出合法性，要在摄入层增加格式信息存在性校验，避免静默错误导致下游Agent自信答错'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
企业Agent处理合规规则、操作手册等内部文档时，现有文档转文本工具会静默丢失作者嵌入在格式中的语义信息（如红色标注的强制要求、高亮的注意事项），导致Agent给出自信但错误的答案，且这类错误无法通过常规链路监控发现，严重影响Agent部署可靠性。

### 方法关键点
- 基于python-docx开发无LLM的格式感知解析器，提取颜色、高亮、粗体等6类格式特征，仅保留高置信度的格式-语义映射（红色/红色高亮→`CRITICAL_WARNING`、任意非白色高亮→`WARNING`等），避免歧义信号误导模型
- 采用混合序列化方案：用Markdown表示预训练覆盖的粗体、斜体等格式，自定义标签表示颜色、高亮等无对应Markdown的格式，同时显式补充页眉、脚注、修订记录等常规解析无法获取的内容
- 采用逐类留一法消融定位影响因子，评价无需LLM裁判，直接和文档原生OOXML属性做确定性匹配，避免评估偏差

### 关键实验结果
数据集覆盖6462份真实政策文档，其中32.8%包含颜色/高亮提示，10.3%的强制要求带格式标记，下游任务为提取作者标记的高优先级要求。对比plain text、docling、docx2python三类主流基线，覆盖Claude全系列、GPT-5.6共6款大模型：
- 格式感知方案micro F1达0.690，docling仅0.150、plain text仅0.075；docling的未标记要求误报率是本文方案的4倍
- 保留格式后附加语义标签比仅保留原始格式标记提升0.085的macro F1
- 仅高亮（贡献+0.302 F1）和颜色（贡献+0.262 F1）两类格式贡献了全部性能收益，其余4类格式影响不足±0.003

最值得记住的结论：对于企业文档处理Agent，可靠性的胜负手在摄入层而非推理层，修复格式丢失问题完全可以用无LLM的代码实现，成本极低且效果可衡量。
