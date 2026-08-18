---
title: 'Every Coin Has Two Sides: On the Dual Nature of Generalization in On-Policy
  Distillation of Large Language Models'
title_zh: 大模型On-Policy蒸馏的泛化二重性研究
authors:
- Zhaoyi Li
- Deyang Kong
- Yuan Wei
- Evan Yang
- Ranran Shen
- Mahardika Krisna Ihsani
- Ming Yang
- Wei Zhang
- Chuan Hao
- Jian Yang
affiliations:
- University of Science and Technology of China
- Peking University
- IQuest Research
- MBZUAI
- Zhejiang University
arxiv_id: '2608.16647'
url: https://arxiv.org/abs/2608.16647
pdf_url: https://arxiv.org/pdf/2608.16647
published: '2026-08-17'
collected: '2026-08-18'
category: Training
direction: 大模型训练 · On-Policy蒸馏优化
tags:
- On-Policy Distillation
- Knowledge Distillation
- LLM Training
- Multi-Teacher Distillation
- Generalization
one_liner: 系统揭示大模型On-Policy蒸馏泛化规律，明确同/异源对差异与多教师OPD跷跷板效应
practical_value: '- 做业务小模型蒸馏对齐时优先选与学生同基模型的同源教师，哪怕性能稍弱也比异源强教师泛化效果好，适合端侧Agent、推荐场景小模型落地

  - OPD训练无需过滤教师解不出的难样本，仅需动态剔除学生已完全掌握的样本，可降低数据准备成本同时小幅提升效果

  - 多场景统一推荐/Agent模型做多教师蒸馏时，不要仅依赖领域路由隔离教师影响，需通过调整教师数据混合比例平衡各域性能

  - 诊断多教师蒸馏的域性能退化时，不要只排查目标域对应教师，需考虑其他教师的跨域拉偏影响，减少调参试错成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有On-Policy蒸馏（OPD）研究大多在单域、与训练数据接近的基准上评估，无法区分局部拟合和全局策略迁移，对跨语言、跨推理长度、跨域的泛化规律认知不足，多教师OPD的效果可控性差，亟需系统的泛化特性研究支撑落地。

### 方法关键点
- 控制变量实验设计，每次仅调整一个泛化因子（训练难度、语言、推理长度、任务域、师生同源性），固定其余条件
- 对比单教师OPD下，同/异源师生对（同基模型/不同基模型）的泛化差异
- 测试多教师OPD（MOPD）的领域路由隔离效果，分析教师数据混合比例对多域性能的影响

### 关键结果数字
实验覆盖数学、代码、科学、指令跟随4大类任务，基准包括BigMath、LiveCodeBench、GPQA-Diamond、IF-Eval等：
1. OPD效果几乎不受训练样本难度影响，教师全解不出的样本与全解对的样本训练后最终准确率差异<1%，极端难度样本也能恢复80%以上的OPD收益
2. 同源教师的跨域泛化效果比异源教师高15%~30%，即便异源教师的 standalone 性能显著强于同源教师
3. 多教师OPD调整数据混合比例可使单域性能波动5%以上，传统领域路由完全无法隔离教师的跨域影响

### 核心结论
On-Policy蒸馏转移的是教师的推理行为而非特定问题的答案，同源师生对实现全局策略对齐，异源师生对仅能局部拟合训练分布，多教师OPD会出现能力跷跷板效应而非简单叠加各教师的领域优势
