---
title: Do Language Models Need a Trainable Input Embedding Table? Fixed Minimal Token
  Codes at 1.7B-Class Scale
title_zh: 1.7B规模验证：语言模型可采用固定Token编码替代可训练输入嵌入表
authors:
- A. Bochkov
arxiv_id: '2610.04002'
url: https://arxiv.org/abs/2610.04002
pdf_url: https://arxiv.org/pdf/2610.04002
published: '2026-10-01'
collected: '2026-10-07'
category: LLM
direction: LLM 输入嵌入层架构优化
tags:
- LLM
- Input Embedding
- Fixed Token Encoding
- Model Optimization
- Decoder-only
one_liner: 1.7B参数规模下验证固定最小Token编码可替代可训练输入嵌入表，保留可观语言建模能力
practical_value: '- 垂直领域小参数LLM/端侧推荐Agent可尝试固定Token编码替代输入嵌入表，减少约5%参数量，降低训练与部署的显存开销

  - GenRec场景下的Semantic ID编码可参考固定二进制编码+无参数重复升维方案，无需额外训练投影层，降低编码模块的训练复杂度

  - 多模态推荐的跨模态Token对齐可将固定身份编码作为基准方案，简化不同模态输入层的兼容设计，降低对齐成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统LLM输入层采用独立可训练的Token嵌入表，约占总参数量的5%，但其架构必要性未得到严格验证；同时固定输入接口可为表征学习、模块化系统设计提供可控的边界条件，因此需要验证固定Token编码能否支撑可观的语言建模能力。

### 方法关键点
- 控制变量训练3组1.7B级Decoder-only模型，共享Tokenizer、主干架构、训练流程，仅输入层存在差异：对照组采用可训练嵌入表，两个实验组分别采用16位最小二进制Token编码、GF(2)域下可逆重编码的固定编码
- 固定编码采用无参数升维方案：将16位编码重复128次匹配2048维隐藏层宽度，无额外可训练输入投影层
- 训练数据为FineWeb-Edu清洗语料，单模型训练预算100B Tokens，评估覆盖HellaSwag、PIQA、LAMBADA等10项标准基准

### 关键结果
- 固定编码模型可删除100.7M参数量（占原模型5.56%），仍保留可观能力：16位二进制编码模型HellaSwag归一化准确率52.40%、PIQA准确率70.51%、LAMBADA准确率42.75%
- 固定编码模型性能略低于可训练嵌入表对照组（对照组HellaSwag 57.79%、LAMBADA 47.72%），GF(2)重编码模型与二进制编码模型性能相当，无显著差距
- 固定编码模型性能介于SmolLM2-135M与SmolLM2-360M之间，为可用的预训练基座模型

### 核心结论
可训练输入嵌入表有用但并非必须，固定Token身份编码即可支撑Transformer主干完成有效的语言建模学习
