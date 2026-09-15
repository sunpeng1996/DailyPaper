---
title: How Good Are Frontier Models at Physics? Expert Re-Grading Reveals Broken Evaluations
  and Near-Saturation of Leading Benchmarks
title_zh: 前沿大模型物理能力评测：专家重判揭示基准失效与任务近饱和
authors:
- Ali Ansari
- Haoran Sun
- Andy Zeyi Liu
- Mark Jabbour
- Yongshan Ding
- Steven Girvin
- Yu He
- Sohrab Ismail-Beigi
- Aleksander Kubica
- Owen D. Miller
affiliations:
- Yale University
- Jump Trading Group
- University of Cambridge
- University of Southern California
arxiv_id: '2609.13009'
url: https://arxiv.org/abs/2609.13009
pdf_url: https://arxiv.org/pdf/2609.13009
published: '2026-09-11'
collected: '2026-09-15'
category: Eval
direction: 大模型科学推理能力评测优化
tags:
- LLM Evaluation
- Scientific Reasoning
- Benchmark Audit
- Expert Grading
- Reasoning Capability
one_liner: 通过专家重判6个主流物理基准，证实原有评测缺陷大幅低估前沿大模型物理推理能力，现有基准已近饱和
practical_value: '- 垂直领域（如电商合规、广告素材审核）LLM能力评测可引入领域专家重判流程，区分模型错误、标注错误、问题歧义，避免低估模型实际可用能力

  - 对内部业务基准定期做专家审计，修正错误标注、剔除歧义任务，避免用有缺陷的基准迭代算法导致方向走偏

  - 若业务闭域结构化任务模型准确率接近饱和，可设计更高难度的专家验证新任务集迭代模型，避免无效调优'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有公开物理基准的低得分指向前沿大模型物理推理能力不足，与领域专家实际使用体验存在偏差，原评测可信度存疑。

### 方法关键点
针对6个主流物理基准的纯文本可验证答案问题，邀请物理子领域专家逐例审核，区分模型真错、打分错误、参考答案错误、题目歧义四类问题，修正基准后重新计算模型得分。

### 关键结果
修正后GPT-5.6-Sol的mean@4在HLE-Physics从47.3%升至78.7%，在CMT-Benchmark从61.0%升至87.2%，CritPt挑战集修正后pass@4达94.4%；其余3个基准的审计子集得分均大幅提升，原基准普遍低估大模型能力，现有闭端任务已近饱和。
