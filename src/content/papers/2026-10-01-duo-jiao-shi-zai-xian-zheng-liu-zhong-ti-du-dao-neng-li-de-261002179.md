---
title: 'From Gradients to Capabilities: Understanding Multi-Teacher On-Policy Distillation'
title_zh: 多教师在线蒸馏中梯度到能力的转化机制解析
authors:
- Siqi Zhu
- Suozhi Huang
- Kaixuan Zhang
- Yuheng Yang
- Zhanyang Jin
- Yihang Sun
- Jiaxuan You
affiliations:
- University of Illinois Urbana-Champaign
- Princeton University
- Westlake University
arxiv_id: '2610.02179'
url: https://arxiv.org/abs/2610.02179
pdf_url: https://arxiv.org/pdf/2610.02179
published: '2026-10-01'
collected: '2026-10-02'
category: Training
direction: 大模型蒸馏训练 · 多教师在线蒸馏
tags:
- Multi-teacher Distillation
- On-policy Distillation
- LLM Training
- Knowledge Distillation
- Optimization
one_liner: 揭示多教师在线蒸馏中损失加权、优化器、精度等因素对能力整合的影响机制
practical_value: '- 做多领域Agent（如电商客服、商品文案生成、跨品类推荐reasoning）的能力整合时，损失加权按需选择：要强化长回复领域能力选全局token平均，要均衡各领域能力选领域响应平均，避免长回复领域权重过高挤压短回复领域效果

  - 用MOPD做垂直领域小模型蒸馏时，优先选用无动量SGD替代Adam，可获得更高的多任务平均得分，还能降低历史梯度的干扰，适配业务快速迭代需求

  - 蒸馏训练时可直接用师生top64词的交集KL替代全词表KL，梯度一致性>99.9%，可大幅降低显存占用和计算开销，适合资源有限的业务finetune场景

  - 业务finetune时注意BF16精度的隐藏效应：如果需要保留稀疏的领域能力增量，建议留存FP32主权重，避免小参数更新被BF16 rounding抹除'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
多教师在线蒸馏（MOPD）是整合多个RL训练的领域专家模型能力的主流方案，但现有实践普遍存在强教师能力无法完全迁移、不同领域能力失衡的问题，教师信号到学生参数更新、最终能力的传导机制尚未明确，导致方案调优缺乏可落地的指导依据。
### 方法关键点
- 控制变量实验设计：以Qwen3-1.7B为学生底座，对齐初始化训练数学、代码、指令跟随、科学4个领域的RL教师，固定学生参数、响应、优化器状态对比不同配置的差异
- 对比3类损失加权策略：全局token平均（GT，长回复权重更高）、领域token平均（DT，固定领域权重但长回复权重更高）、领域响应平均（DR，领域内响应权重相等）
- 对比3类蒸馏损失：采样token PG损失、top-k师生词表交集KL损失、全词表KL损失
- 单独验证Adam一阶动量、BF16数值精度对参数更新的影响
### 关键结果
在MATH-500、LiveCodeBench、IFBench、GPQA四个基准上测试：
1. 不同损失加权的原始梯度余弦相似度仅0.68，经Adam一阶动量处理后更新方向余弦相似度升至0.96，动量大幅抹平不同教师信号的差异
2. FP32主权重有97%与初始化不同，经BF16 rounding后仅7~11%的参数存在差异，小参数更新会被低精度隐藏
3. top-64交集KL的梯度与全词表KL梯度余弦相似度>0.999，在DR加权下数学准确率比PG损失高2.6pp，在GT加权下低2.1pp
4. 无动量SGD的四任务平均得分比Adam高0.47~1.03pp，更适配MOPD训练
### 核心结论
梯度保真度高不代表最终任务效果一定更好，MOPD的能力整合效果是损失加权、优化器、词表选择共同作用的结果，需结合目标领域需求搭配配置
