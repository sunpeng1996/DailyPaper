---
title: 'RSI Arena: Towards Recursive Self-Improvement with Human Feedback'
title_zh: 《RSI Arena：探索基于人类反馈的大模型递归自改进框架》
authors:
- Yue Huang
- Yanbo Wang
- Lichi Li
- Yuanyuan Chen
- Andreas Haupt
- Xiaonan Luo
- Zheyuan Liu
- Jihye Choi
- Felix Juefei-Xu
- Xiangliang Zhang
affiliations:
- Bake AI
- University of Notre Dame
- Stanford University
- Hugging Face
- NVIDIA Research
arxiv_id: '2610.33624'
url: https://arxiv.org/abs/2610.33624
pdf_url: https://arxiv.org/pdf/2610.33624
published: '2026-10-23'
collected: '2026-10-28'
category: Agent
direction: Agent 自主大模型训练与自改进
tags:
- Autonomous Agent
- Self-Improvement
- Human Feedback
- LLM Post-Training
- Benchmark
one_liner: 搭建两阶段多Agent自主后训练平台，验证基于人类反馈的大模型递归自改进可行性
practical_value: '- 用户偏好评估可参考文本长度、格式（列表/加粗）的校正逻辑，消除投票中的样式偏差，避免推荐/广告文案排序被冗余长度误导

  - 做基于用户反馈的模型迭代时无需盲目堆算力，19GPU-h训练的模型效果超过部分用满1000GPU-h的模型，优先优化数据选择和训练策略性价比更高

  - 模型效果评估要结合自动benchmark和人工盲测，LLM判分的chat类benchmark（如WildBench）和人工偏好相关性可达0.95，可作为离线快速评估指标替代部分高成本人工评估

  - 电商场景的Agent自主迭代可参考两阶段框架：先基于公开数据做SFT+偏好优化，再用真实用户反馈做二次迭代，80%的模型可通过该流程缩小和SOTA的差距'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
递归自改进是大模型发展的长期方向，但现有Agent训练任务多针对单一benchmark、资源约束宽松，未验证Agent能否在真实资源限制下端到端训练出符合人类偏好的可用模型。

### 方法关键点
- 两阶段设计：Stage1给10个前沿大模型Agent相同的基础模型（Nemotron 3.5 30B MoE）、1000GPU-h、300美元API额度，自主完成数据选择、训练、checkpoint选择；Stage2给每个Agent其Stage1模型的人类盲测反馈，追加500GPU-h、150美元API额度做二次迭代
- 评估体系：20个覆盖能力、安全的benchmark + 匿名人类盲测竞技场，同时提供带样式控制（长度、列表、加粗）和不带样式控制的两套Elo评分
- 完全自主规则：无人工干预训练流程，仅最终模型由人类和benchmark评估，避免奖励黑客

### 关键结果数字
- Stage1最优模型（GPT-6 Astra训练）在12个能力benchmark上填平了基础模型到NVIDIA Instruct的76%差距，样式校正后人类偏好评分和NVIDIA Instruct持平
- Stage2中8/10的模型进一步缩小了和NVIDIA Instruct的差距，中位数提升28个Elo分，其中DeepSeek训练的模型人类偏好评分提升172分
- 算力消耗和最终效果无显著相关性（ρ=-0.21），仅用19GPU-h训练的Gemini模型评分超过2个用满1000GPU-h的模型
- 自动benchmark和人类偏好相关性仅0.72，其中WildBench等LLM判分的chat类benchmark相关性可达0.95，数学类benchmark相关性接近0

**最值得记住的一句话**：用户偏好和自动benchmark测的是完全不同的维度，基于人类反馈的迭代能大幅提升用户满意度，但不会带来自动benchmark的显著提升
