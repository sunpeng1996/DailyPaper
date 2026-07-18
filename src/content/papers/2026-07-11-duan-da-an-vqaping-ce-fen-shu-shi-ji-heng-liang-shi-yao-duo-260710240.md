---
title: What Does Your Short-Answer VQA Score Actually Measure? Evaluator-Dependent
  Instability in Multimodal Short-Answer Benchmarks
title_zh: 短答案VQA评测分数实际衡量什么？多模态短答案基准的评估依赖不稳定性
authors:
- Guanhua Ye
- Niu Jingbin
- Yan Li
- Meiyu Liang
- Zhe Xue
- Yingxia Shao
- Yawen Li
affiliations:
- Beijing University of Posts and Telecommunications
arxiv_id: '2607.10240'
url: https://arxiv.org/abs/2607.10240
pdf_url: https://arxiv.org/pdf/2607.10240
published: '2026-07-11'
collected: '2026-07-18'
category: Eval
direction: 多模态评测 · VQA基准稳定性分析
tags:
- VQA
- Multimodal
- Evaluation
- Benchmark
- Semantic Matching
one_liner: 跨6模型6基准审计，揭示短答案VQA评测因表面形式匹配误判语义正确答案的问题
practical_value: '- 电商多模态商品问答、导购Agent的自动评估环节，可在字符串匹配基础上增加低成本语义校验层，避免误判语义正确但表述不同的答案，提升评估准确率

  - 针对不同答案类型设置差异化评估规则：标量类答案（如价格、数量）用严格匹配，提取式/多片段答案（如商品属性、活动规则）放宽表面形式要求，优先校验语义一致性

  - 业务自动评测流程可补充CPU即可运行的确定性修复规则，批量修正表面形式不匹配导致的误判，减少人工复核成本'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有短答案VQA基准的自动评估混淆「答案语义正确性」和「与预设答案表面形式匹配度」两个维度，导致评测结果存在不可解释的偏差，可信度不足。
### 方法关键点
跨6个视觉语言模型、6个VQA基准开展审计，使用精度97.6%的人工校验语义判定器审核超过3.7万条官方判定的错误样本，同时引入第二套纯文本判定器复现结果排除单模型偏差，还验证了提示/上下文改写对评测稳定性的影响，最终用无GPU依赖的确定性规则尝试修复误判。
### 关键结果数字
文本密集型基准中最高50%的官方错误实际为语义正确、仅表面形式不匹配的样本；提取式、多片段答案的评估敏感度远高于标量答案；无任务变更的良性提示改写会大幅翻转单样本评测结果；确定性规则可部分修复误判，提升评测结果可信度
