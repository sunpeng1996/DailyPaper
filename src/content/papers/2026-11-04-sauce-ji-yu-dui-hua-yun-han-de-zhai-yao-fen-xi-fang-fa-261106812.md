---
title: 'SAUCE: Summary Analysis Using Conversation Entailment'
title_zh: SAUCE：基于对话蕴含的摘要分析方法
authors:
- Man-Ling Sung
- Hemanth Kandula
- Jeff Ma
- William Hartmann
- Matthew Snover
affiliations:
- RTX BBN Technologies
arxiv_id: '2611.06812'
url: https://arxiv.org/abs/2611.06812
pdf_url: https://arxiv.org/pdf/2611.06812
published: '2026-11-04'
collected: '2026-11-05'
category: Eval
direction: LLM对话摘要评估 · 无参考可解释
tags:
- LLM
- Evaluation
- Summarization
- Entailment
- Interpretability
- Reference-free
one_liner: 提出无参考可解释的跨语言对话语音摘要评估管线，对齐人类判断
practical_value: '- 可复用对话蕴含的事实校验思路，用于LLM生成的商品文案、客服对话摘要的幻觉检测，避免虚假宣传风险

  - 无参考评估框架可直接迁移到生成式推荐的item描述、用户兴趣摘要的离线效果评测，无需构造大量标注参考

  - 离散事实映射的可解释性设计，可用于生成式推荐bad case归因，快速定位内容错漏点优化模型效果'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
开放无明确目标的对话摘要缺乏有效评估方案，传统依赖参考摘要的指标无法适配多样的摘要正确性分布，黑盒LLM评估或密集嵌入类指标无解释性，难以精确定位幻觉、内容遗漏问题，跨语言语音场景下转录翻译误差的影响也难以被现有指标捕捉。
### 方法关键点
SAUCE是无参考、事实驱动的跨语言对话语音摘要评估管线，通过对话原文与摘要文本的蕴含关系计算摘要的准确率、事实覆盖率，将评分直接映射到离散可验证的事实节点，天然支持错误点定位。
### 关键结果
相比主流摘要评估指标，可精准识别转录、翻译误差导致的信息损失与低质量摘要；初步实验显示与人类判断的对齐度显著优于基线方案，且具备完全可解释性，可直接用于LLM行为画像与实际场景摘要校验。
