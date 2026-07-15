---
title: Extractable Memorization From First Principles
title_zh: 基于第一性原理的大模型可提取记忆研究
authors:
- A. Feder Cooper
- Marika Swanberg
- Jamie Hayes
- Lea Duesterwald
- Christopher De Sa
- Daniel E. Ho
- Mark A. Lemley
- Percy Liang
arxiv_id: '2607.12649'
url: https://arxiv.org/abs/2607.12649
pdf_url: https://arxiv.org/pdf/2607.12649
published: '2026-07-14'
collected: '2026-07-15'
category: LLM
direction: 大模型可提取记忆检测与校准
tags:
- LLM
- Memorization Detection
- Conformal Test
- Threshold Calibration
- Data Leakage
one_liner: 提出两种匹配比较校准方法，解决现有LLM可提取记忆研究的有效性偏差问题
practical_value: '- 电商/广告场景微调专属LLM（文案生成、推荐理由生成）时，可复用匹配比较方法检测训练数据泄露，避免商家敏感信息、版权内容被不当提取

  - 搭建RAG系统时，可参考该非训练序列基线思路，区分LLM原生训练记忆和外挂知识库知识，降低生成内容的幻觉率和侵权风险

  - 开发LLM驱动的推荐Agent时，可使用校准后的记忆阈值做输出过滤，避免用户隐私数据、历史训练数据被意外生成泄露'
score: 8
source: arxiv-cs.CL
depth: abstract
---

## 动机
现有LLM可提取记忆研究存在两类有效性偏差：一类用过短序列无法区分记忆和文本可预测性，高估提取率；另一类将模型生成未训练过的真实文本视为提取不可靠，低估记忆判定的可行性，两类都缺失匹配非训练序列生成概率作为可预测性基线的核心逻辑。
## 方法关键点
提出两种校准的匹配比较方案：1）共形测试：当训练/非训练序列从群体采样时，可将阈值校准到指定FPR；2）普查法：针对单文档（如书籍）场景，匹配同类非训练文档做基线校准。
## 关键结果
OLMo 2 32B在Wikipedia数据集上生成非训练10-token后缀的频率为训练序列的24%，该部分全部为假阳性；Llama 3.1 70B在书籍场景下校准的记忆判定阈值低至1e-27，可识别常规采样预算无法覆盖的记忆序列。
