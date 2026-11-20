---
title: Can LLMs Resolve Entity Conflicts in Domain Specific NLU Pipelines?
title_zh: 大语言模型能否解决领域特定NLU流水线中的实体冲突问题
authors:
- Akansha Bhardwaj
- Mingbo Cui
- Victor Guimaraes
- Dominik Kohler
- Diana Nicoleta Popa
- Meghana M. Reddy
- Paolo Rosso
affiliations:
- Telepathy Labs GmbH, Zürich, Switzerland
arxiv_id: '2611.25733'
url: https://arxiv.org/abs/2611.25733
pdf_url: https://arxiv.org/pdf/2611.25733
published: '2026-11-19'
collected: '2026-11-20'
category: LLM
direction: 大语言模型 · 领域NLU实体消歧
tags:
- LLM
- LoRA
- Entity Resolution
- NLU
- In-Context Learning
one_liner: 对比规则基线、Llama3.1-8B多轮提示与LoRA微调方案，验证LLM可替代领域NLU实体冲突消歧规则系统
practical_value: '- 电商/客服Agent场景下的多NER抽取器冲突消歧，可直接复用「LoRA微调+2~7 shot检索式示例提示」的混合方案，替代难维护的规则系统，大幅降低迭代成本

  - 针对不同场景做性能拆分：通用场景（如时间协商、地址识别）可直接用多shot提示兜底，高领域专属场景（如商品SPU识别、服务项匹配）优先做LoRA微调，资源投入效率最高

  - 多shot提示的示例选择优先用语义检索召回的相似case，比人工curated示例性能更稳定，尤其适配商品、车型等实体相似度高的领域场景

  - 无标注数据时可先用现有规则系统的输出做弱监督训练LoRA，能快速达到和规则基线80%+的匹配度，再用少量人工标注迭代即可超过规则性能'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
领域特定NLU流水线通常部署多个并行NER抽取器覆盖不同实体类型，但易出现重叠span实体类型冲突，传统规则/优先级排序方案维护成本极高，新增实体或场景时易冲突，亟需可扩展的替代方案。

### 方法关键点
- 对比三类方案：传统规则基线、Llama3.1-8B-Instruct多shot提示（含人工curated示例和语义检索召回示例两种）、LoRA微调后的Llama3.1-8B-Instruct多shot提示
- 输入仅需原始文本、多NER抽取器输出、对话上下文标签，不依赖NER抽取器内部实现，适配黑盒抽取器场景
- 微调数据集来自真实对话系统的6万+标注样本，验证集覆盖汽车详情、服务请求、时间协商三类对话场景

### 关键结果数字
- Automotive-Rule-Based数据集（规则系统输出为标签）：LoRA微调+2shot提示方案达到和规则基线81.42%的匹配度，远高于base模型8.92%的0shot水平
- Automotive-Curated数据集（人工标注金标准，674条）：最优LLM方案（LoRA微调+7shot提示）整体准确率78.93%，略高于规则基线的78.60%；其中时间协商场景领先规则基线8.27%，服务请求等强领域场景略低于规则基线5.6%
- 语义检索召回的多shot示例比人工curated示例性能更稳定，在汽车实体等相似度高的场景下表现更优

### 最值得记住的一句话
LLM替代领域实体冲突消歧规则系统的最优方案是「LoRA微调+检索式多shot提示」的混合策略，通用场景用提示快速适配，领域场景靠微调保障精度，平衡灵活性和性能
