---
title: 'Know When to Stop: Segment-Level Credit Assignment for Reducing Overthinking'
title_zh: 知止：基于片段级信用分配的大模型过度思考抑制方法
authors:
- Chia-Hsuan Lee
- Sihui Dai
- Mingyang Zhou
- Isha Slavin
- Hsuan Su
- Shi-Xiong Zhang
- Sambit Sahu
- William Campbell
affiliations:
- Capital One
arxiv_id: '2607.00482'
url: https://arxiv.org/abs/2607.00482
pdf_url: https://arxiv.org/pdf/2607.00482
published: '2026-08-03'
collected: '2026-08-06'
category: Reasoning
direction: 推理大模型 · RL训练优化
tags:
- LLM Reasoning
- GRPO
- Credit Assignment
- Overthinking
- Reinforcement Learning
one_liner: 提出无额外标注的片段级信用分配算法DASH 抑制推理大模型过度思考提升准确率
practical_value: '- 片段级信用分配思路可迁移至多步推理Agent的RL优化：如电商导购Agent多轮搜索、下单决策场景，将完成子目标的轨迹片段单独分配正负奖励，替代全轨迹统一打分，减少冗余操作同时提升任务完成率

  - 论文提出的6种基于规则的无监督过度思考信号（重复、对冲、策略放弃、自相矛盾、重复计算、长度异常），可直接复用做电商智能客服、RAG导购系统的生成质量巡检，无需训练额外奖励模型即可快速识别无效推理

  - 漂移轨迹的奖励塑形方法可复用至生成式推荐的RLHF训练：对推荐结果部分匹配用户需求的失败轨迹按匹配度给部分奖励，替代全负标签，提升训练样本利用率，降低标注成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
推理大模型依赖长思维链提升效果，但普遍存在过度思考问题：出现对冲、策略放弃、自相矛盾等无效行为，甚至得到正确中间答案后反复修正最终答错；现有解决方案要么需要昂贵的步骤级标注，要么仅靠长度惩罚，容易误伤有效长推理，亟需低成本的细粒度信用分配方案。
### 方法关键点
- 提出DASH算法，无需额外标注，通过匹配固定模式抽取推理轨迹中的中间答案checkpoint，将轨迹拆分为多个独立片段
- 片段级差异化优势分配：产出正确答案的片段给正奖励（重复确认的正片段奖励几何衰减，避免鼓励冗余验证）；产出错误答案的片段给随长度递增的负奖励；存在正确到错误漂移的失败轨迹，其正确推理前缀给弱正奖励，避免惩罚有效思考
- 漂移轨迹奖励塑形：按正确片段占比给部分奖励，排名高于完全错误轨迹，大幅提升失败样本的利用率
### 关键实验
在4个竞赛级数学推理基准上测试，对比base模型、GRPO、DR-GRPO等基线：
- DR-GRPO+DASH平均准确率达59.45%，较DR-GRPO提升1.32pp，较标准GRPO提升2.5pp
- 自校正率是GRPO的2倍，策略放弃行为减少41%，对冲行为减少14%，长度异常减少17%
- 适配3种不同架构、不同规模的推理模型，均获得一致的准确率提升

> 最值得记住的结论：高效推理训练不应一味要求模型输出更短，而应教会模型识别什么时候反思不再有用。
