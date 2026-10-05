---
title: Predicting and Repairing Merge Collapse in Large Language Models
title_zh: 大语言模型合并崩溃的预测与修复方法PRISM
authors:
- Jungseob Lee
- Seungyoon Lee
- Sugyeong Eo
- Hyeonseok Moon
- Jaehyung Seo
- Heuiseok Lim
affiliations:
- Korea University
- Yonsei University Mirae Campus
- Sookmyung Women's University
- Konkuk University
arxiv_id: '2610.03199'
url: https://arxiv.org/abs/2610.03199
pdf_url: https://arxiv.org/pdf/2610.03199
published: '2026-10-02'
collected: '2026-10-05'
category: LLM
direction: LLM多任务模型合并优化
tags:
- model_merging
- task_vector
- soft_thresholding
- LLM
- weight_averaging
one_liner: 提出无数据的预合并崩溃预测指标与PRISM算子 避免多任务LLM合并时性能暴跌
practical_value: '- 合并多个垂直领域微调的LLM（如电商的商品理解、营销文案、客服应答模型）前，可先用论文提出的interference score预检查合并是否会崩溃，无需等合并后再评测，大幅节省计算和时间成本

  - 合并多专家模型时可复用PRISM的「先平均任务向量再按层做interference校准软阈值」策略，无需额外标注数据或调参，即可避免合并后性能暴跌，效果优于TIES、DARE等传统先剪枝再合并的方法

  - 借鉴ρ-gate设计，当任务向量冲突以单侧漂移（某专家独有知识更新，其他专家无对应修改）为主时直接用普通平均，无需阈值处理，保住单任务特有能力（如推荐系统的冷门兴趣理解、合规风控规则等特有知识）'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
同基座微调的多领域LLM通过任务向量平均合并是低成本融合多能力的常用方案，但常出现合并后性能远低于基座的崩溃问题，现有方法无预合并预警，只能事后评测发现，浪费大量计算资源。
### 方法关键点
- 提出预合并崩溃预测指标`interference score`：即多专家任务向量的方差，仅需权重和数分钟CPU计算即可提前判断合并是否会发生破坏性崩溃
- 设计PRISM合并算子：先对归一化后的任务向量做平均，再根据每层的interference值用Donoho-Johnstone通用软阈值去噪，仅保留幅度超过阈值的更新，同时设置0.1%的保留率下限避免过度剪枝
- 新增ρ-gate机制：当冲突主要来自单侧漂移而非符号相反的抵消时，直接返回普通平均结果，保留单任务特有知识
- 全程无需额外训练数据、超参数调优，仅依赖权重统计信息
### 关键结果
在4个模型家族22种合并配置下测试：1. `interference score`阈值1.9e-3可100%区分15个无害合并和5个破坏性合并，14个前瞻性测试案例预测准确率达85.7%；2. PRISM在Qwen2.5-7B数学+代码专家合并场景下，6任务平均得分67.8，比普通平均高18.3pp，比TIES高6.7pp；3. 所有破坏性合并经PRISM修复后性能接近基座，而普通平均至少低14.4pp甚至完全崩溃。
> 最值得记住：先合并再剪枝比先剪枝再合并更能保留跨任务有效知识，合并前先算任务向量方差即可提前规避崩溃风险
