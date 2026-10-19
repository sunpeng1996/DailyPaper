---
title: 'Truth in Contrast: Calibrated Factual Evidence from Language Model Likelihoods'
title_zh: 基于对比生成似然的大语言模型事实置信度校准方法
authors:
- Ponhvoan Srey
- Jason Lucas
- Pittawat Taveekitworachai
- Junyoung Lee
- Anh Tuan Luu
affiliations:
- Nanyang Technological University
- University of Colorado at Boulder
- National University of Singapore
- VinUniversity
arxiv_id: '2610.23527'
url: https://arxiv.org/abs/2610.23527
pdf_url: https://arxiv.org/pdf/2610.23527
published: '2026-10-16'
collected: '2026-10-19'
category: LLM
direction: LLM事实性评估 · 置信度校准
tags:
- Factual Calibration
- Contrastive Likelihood
- Cross-lingual Transfer
- Confidence Estimation
- LoRA
one_liner: 通过对比事实与非事实条件下的文本似然，得到校准更优的LLM事实置信度并实现无标注跨语言迁移
practical_value: '- 做Agent生成内容的事实性校验时，可复用CFP方法：将生成的输出分别拼接「要求生成事实正确内容」「要求生成错误内容」两个prompt前缀，计算似然差得到校准后的事实置信度，无需额外训练即可过滤幻觉内容，比直接询问LLM内容是否正确的方案更稳定

  - 做多语言电商站点的商品介绍、营销文案生成时，可借鉴几何对齐思路：以中文/英文等高资源语言的事实性信号为锚点，仅对齐目标语言与高资源语言在事实证据方向的CFE值，用LoRA微调小参数，无需目标语言的事实标注即可提升小语种生成内容的事实准确率，同时不影响通用生成能力

  - 做推荐系统的生成式商品卖点、搜索query自动补全时，可用CFP的校准特性设置阈值，当置信度低于阈值时触发RAG检索商品真实参数、历史搜索词库，避免生成错误的商品信息、无效搜索词，降低客诉和搜索跳出率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM预训练阶段内置了大量事实知识，但生成内容易出现幻觉，现有事实置信度估计方法存在两类缺陷：基于预测不确定性的方法无法准确跟踪事实正确性，基于直接询问的P(True)类方法受prompt设计、模型后训练影响大，两类方法都无法同时保证良好的区分度（准确排序事实/非事实）和校准度（置信度数值对应真实正确概率），且在低资源语种下性能下降明显。

### 方法关键点
- 提出对比事实证据（CFE）：将同一段文本分别作为「事实正确」「事实错误」两类prompt前缀的续文，计算两个条件下的文本似然差作为事实性信号，可抵消文本词频、长度等跨条件共享的误差
- 推导对比事实后验（CFP）：将CFE经sigmoid映射为[0,1]区间的校准后验概率，理论证明当两类条件的似然误差高度相关时，CFP的校准误差下界更紧
- 提出几何引导的跨语言事实对齐：将似然空间分解为事实证据方向和证据无关正交方向，仅对齐目标语言与高资源语言（如英语）在事实证据方向的CFE值，用LoRA微调无需目标语言事实标注

### 关键实验
实验基于多语言True-False数据集，覆盖8种语言共4.8万条事实陈述，对比9种主流基线（MSP、P(True)、Gen-Z等），在12款0.6B-14B参数的LLM上测试。结果显示：CFP平均ECE为0.115，较最优基线P(True)-norm的0.206低44%，AUROC达0.689与基线持平；跨语言迁移实验中，Qwen-3.5-4B的印地语事实区分度从57.0提升至70.5，填补44%与英语的性能gap，同时通用阅读任务Belebele准确率几乎无损失。

### 最值得记住的结论
对比互补条件下的似然差可抵消通用噪声，得到更可靠的特定属性（如事实性）置信度，无需目标领域标注即可实现跨语言/跨场景迁移。
