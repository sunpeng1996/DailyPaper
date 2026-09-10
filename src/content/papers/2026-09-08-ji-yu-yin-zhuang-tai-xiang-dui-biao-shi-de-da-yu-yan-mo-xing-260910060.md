---
title: Reference-Based Bias Detection in LLMs via Relative Representations of Hidden
  States
title_zh: 基于隐状态相对表示的大语言模型参考式偏差检测
authors:
- Marek Jeliński
- Jan Dubiński
- Maciej Chrabaszcz
- Sebastian Cygert
affiliations:
- NASK - National Research Institute, Poland
- Warsaw University of Technology, Poland
- Gdańsk University of Technology, Poland
arxiv_id: '2609.10060'
url: https://arxiv.org/abs/2609.10060
pdf_url: https://arxiv.org/pdf/2609.10060
published: '2026-09-08'
collected: '2026-09-10'
category: Eval
direction: 大语言模型 · 偏差检测评估
tags:
- LLM Bias Detection
- Hidden State Representation
- Fine-tuning Audit
- Model Safety
- Efficient Evaluation
one_liner: 通过锚句相对隐状态表示计算ΔB，低成本快速检测LLM微调前后的偏差变化
practical_value: '- 业务场景LLM微调后合规检测可复用相对隐状态表示思路，无需大量标注评估集即可快速检测偏见、歧视性输出风险，大幅降低审核成本

  - 上线Agent/生成式推荐的LLM服务前，可用ΔB指标快速校验不同微调版本的偏差变化，提前拦截偏差升高的模型checkpoint，规避舆情风险

  - LoRA等参数高效微调后的模型偏差检测，可仅保留业务相关的属性/目标组锚点适配该方法，进一步压缩检测耗时到分钟级'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有LLM偏差审计依赖输出层检测，需高成本标注基准或裁判模型，易漏检未体现在生成文本的内部表征偏差，且微调后隐状态几何结构变化，无法直接跨版本比较。
### 方法关键点
基于固定锚句集合，将各版本模型的隐状态编码为与锚句的相似度向量，得到统一空间下的相对表示；计算目标群体与正负属性关联的偏移量，定义为表征偏差偏移ΔB。
### 关键结果
18组测试中15组ΔB与输出层偏差变化强相关，全微调场景下相关系数|r|达0.84；偏差升高checkpoint检测ROC AUC为0.65~0.99，效果优于SEAT基线；单模型检测仅需3分钟，算力开销比输出层基准低3~50倍，锚点、属性模板变更时指标稳定。
