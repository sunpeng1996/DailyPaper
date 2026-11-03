---
title: 'Meet Students Where They Are: Student-Prefix Teacher Adaptation for On-Policy
  Distillation'
title_zh: 学生前缀教师自适应SPTA：提升On-Policy知识蒸馏的监督质量
authors:
- Xue Zhang
- Songming Zhang
- Yunlong Liang
- Fandong Meng
- Yufeng Chen
- Jinan Xu
affiliations:
- Beijing Jiaotong University
- Weixin AI, Tencent
arxiv_id: '2611.03133'
url: https://arxiv.org/abs/2611.03133
pdf_url: https://arxiv.org/pdf/2611.03133
published: '2026-11-02'
collected: '2026-11-03'
category: Training
direction: LLM训练 · On-Policy蒸馏优化
tags:
- Knowledge Distillation
- On-Policy Distillation
- RLVR
- Teacher Adaptation
- LLM Training
one_liner: 通过让教师预适配学生生成的前缀，提升On-Policy知识蒸馏的监督可靠性与学生性能
practical_value: '- 轻量化LLM/Agent蒸馏时，可在标准On-Policy蒸馏前，先基于学生生成的随机截断前缀，用业务可验证奖励（点击/转化/答案正确性）微调教师模型，无需修改原有蒸馏流程即可提升监督质量

  - 生成式推荐/Query推荐的小模型蒸馏遇到效果瓶颈时，优先评估教师在学生生成前缀下的表现，而非仅依赖教师的 standalone 性能指标

  - 蒸馏时无需过滤学生的错误前缀，直接让教师学习从任意学生前缀生成正确结果，可省去错误检测成本，同时提升教师对学生分布的适配性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
On-Policy蒸馏（OPD）通过在学生生成轨迹上优化缓解曝光偏差，但学生前缀可能包含推理错误或教师不熟悉的模式，导致教师token级监督可靠性随前缀长度增加显著下降，现有方法多从学生侧调整监督策略，未解决教师侧的分布不匹配问题。

### 方法关键点
- 两阶段流程：第一阶段先做前缀条件的教师适配，收集学生生成的轨迹，随机截断为不同长度的前缀，用RLVR（带可验证奖励的强化学习）训练教师基于这些前缀生成正确后续内容，奖励仅看最终结果正确性，允许教师纠正学生错误而非模仿学生
- 第二阶段冻结适配后的教师，沿用标准On-Policy蒸馏流程，无需修改蒸馏目标
- 支持迭代优化：蒸馏后用更新后的学生重新生成前缀，再做一轮教师适配+蒸馏，可进一步提升效果

### 关键结果
在5个数学推理基准（AIME24/25、AMC23、HMMT24/25）上测试3组师生对，对比标准OPD、带任务级RLVR的OPD基线：
- 单轮SPTA比标准OPD平均准确率最高提升3.78个百分点，在标准OPD接近无提升的师生对中，SPTA将增益从0.62拉到3.65个百分点
- 适配后的教师在学生前缀占比90%的场景下，恢复准确率最高提升25.32个百分点，对前缀长度的敏感度大幅下降

**最值得记住的一句话**：教师模型的独立性能不代表其在On-Policy蒸馏中的监督效果，适配学生实际访问的状态比单纯提升教师独立能力更重要。
