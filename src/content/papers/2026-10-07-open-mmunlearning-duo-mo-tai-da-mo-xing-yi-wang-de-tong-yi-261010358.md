---
title: 'Open-MMUnlearning: Unifying Methods and Evaluation for MLLM Unlearning'
title_zh: 《Open-MMUnlearning：多模态大模型遗忘的统一方法与评估框架》
authors:
- Junkai Chen
- Yuhao He
- Qianshan Wei
- Junxiang You
- Jingwen Shao
- Junkai Lin
- Zhongkai Yue
- Xiaotian Ye
- Zhengbo Jiao
- Jiali Cheng
affiliations:
- Institute of Automation, Chinese Academy of Sciences
- ByteDance
- The Chinese University of Hong Kong
- University of Cambridge
- The University of Hong Kong
arxiv_id: '2610.10358'
url: https://arxiv.org/abs/2610.10358
pdf_url: https://arxiv.org/pdf/2610.10358
published: '2026-10-07'
collected: '2026-10-08'
category: LLM
direction: 多模态大模型 · 机器遗忘
tags:
- MLLM
- Machine Unlearning
- Evaluation Framework
- Benchmark
- Metric Reliability
one_liner: 开源统一多模态大模型遗忘框架，集成多类方法与基准，给出方法与评估度量的可靠性对比
practical_value: '- 业务侧MLLM需清除敏感/版权/违规信息时，可直接复用框架内置的12种遗忘算法，优先选GD（侧重遗忘效果）或MIP-Editor（侧重原有能力留存）

  - 评估遗忘效果时可复用论文验证的高可靠度量：优先用BLEU做综合评估，需要高可信度知识留存检验时选KS-Test

  - 可复用框架的鲁棒性评估套件，完成遗忘后MLLM的对抗输入防御、成员推理攻击防御能力测试，满足合规要求

  - 自研遗忘算法时可基于该框架做标准化对比，避免重复实现基准、评估逻辑，降低研发成本'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
MLLM落地时隐私、安全、版权风险凸显，现有机器遗忘方案实现碎片化、评估标准不统一、鲁棒性测试缺失、度量可靠性无共识，难以系统性迭代。
### 方法关键点
开源可扩展框架Open-MMUnlearning统一集成MLLM准备、多模态数据处理、遗忘执行、全链路评估模块，支持4个系列共8款MLLM、12种遗忘算法、覆盖隐私/安全/版权的5类基准，评估维度包含遗忘效果、能力留存、干预鲁棒性、对抗输入鲁棒性、成员推理攻击防御能力，额外设计度量元评估协议验证指标的可信度与鲁棒性。
### 关键结果
10种代表性遗忘方法对比中，GD与MIP-Editor总分并列第一，GD遗忘质量最优，MIP-Editor原有能力留存最好；13种评估度量中BLEU综合可靠性最高，KS-Test可信度AUC最高但鲁棒性稍弱。
