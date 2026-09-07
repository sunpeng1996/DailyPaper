---
title: 'EuroAlpaca: Task-Preserving Localisation of Instruction Data for European
  Languages'
title_zh: EuroAlpaca：保留任务语义的欧洲多语言指令数据本地化流水线与资源
authors:
- Aleix Sant
- Jordi Luque
- Carlos Escolano
affiliations:
- Telefónica Innovación Digital
- Universitat Politècnica de Catalunya
arxiv_id: '2609.05043'
url: https://arxiv.org/abs/2609.05043
pdf_url: https://arxiv.org/pdf/2609.05043
published: '2026-09-04'
collected: '2026-09-07'
category: Training
direction: 多语言LLM指令微调 · 训练数据构建
tags:
- multilingual_LLM
- instruction_tuning
- LoRA
- data_localization
- evaluation_benchmark
one_liner: 提出任务保留的多语言指令本地化流水线，开源覆盖50种欧洲语言的指令数据集与评测基准
practical_value: '- 做多语言场景的LLM Agent/推荐文案生成时，不要直接全量翻译英文指令数据集，要对语法纠错、固定输出标签、代码/ID类字段做保留或任务等价重构，避免训练后指令遵循能力下降

  - 多语言指令微调的效果评估不能只看ROUGE/BERTScore这类参考相似度指标，必须补充可验证的指令遵循准确率评测（类似IFEVAL），避免出现指标好看但实际任务效果差的问题

  - 可复用分层路由流水线：先判断样本是否适合直接翻译，再对字段做翻译/保留决策，不适合的做任务级重写，最后做一致性校验，大幅提升多语言训练数据质量'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有多语言指令微调方案大多直接翻译英文指令数据集，但翻译过程会破坏任务关键约束：语法纠错样本翻译后原错误被自动修正、押韵/字数等形式约束失效、分类标签/代码/ID等固定字段翻译后格式错乱，最终导致训练出的模型参考类指标表现好，但实际指令遵循准确率大幅下降，同时缺乏覆盖多欧洲小语种的统一指令遵循评测基准。

### 方法关键点
- 分层路由处理流水线：基于Alpaca Cleaned的51760条英文样本，先做任务/域语义标注，判断样本走字段级翻译路由还是任务级本地化路由
- 字段级翻译策略：对适合翻译的样本，为instruction/input/output三个字段分别标注TRANSLATE/PRESERVE标签，代码、Semantic ID、固定输出分类标签、翻译任务源文本等字段直接原样保留
- 任务级本地化策略：对依赖源语言形式的样本（语法纠错、押韵、成语、字符/字数约束等），直接在目标语言重构等价任务，保留任务类型、难度、约束和答案对应关系
- 配套构建覆盖50种欧洲语言的EUROPEAN-IFEVAL评测基准，统一可验证指令遵循能力的评测标准

### 关键实验结果
选取4款3-4B参数的主流多语言指令LLM做LoRA微调，对比直接全量翻译、任务保留中间版本、EUROALPACA三个训练集的效果：直接全量翻译相比未适配基线，EUROPEAN-IFEVAL准确率相对下降29.8%，但ROUGE-L、FBERT指标上升；EUROALPACA相比未适配基线，EUROPEAN-IFEVAL准确率提升12.9%，同时ROUGE-L比直接翻译高0.02、FBERT高0.01，在全部200组模型-语言对比中指令遵循能力均优于直接翻译。

### 核心结论
多语言指令数据构建的核心是保留任务语义而非逐字翻译准确，必须同时参考参考相似度类指标和可验证指令遵循指标评估效果，避免出现指标虚高但实际业务效果差的问题。
