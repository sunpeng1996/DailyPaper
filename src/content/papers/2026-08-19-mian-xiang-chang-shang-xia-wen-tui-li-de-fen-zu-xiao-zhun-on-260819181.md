---
title: 'Beyond Teacher Likelihood: Group-Calibrated On-Policy Distillation for Long-Context
  Reasoning'
title_zh: 面向长上下文推理的分组校准On-Policy蒸馏方法GC-OPD
authors:
- Zhu Zhang
- Jixun Wang
- Xiaoang Xu
- Xiaorong Wang
- Zihan Zhou
- Zhiyuan Wang
- Shuo Wang
- Chaojun Xiao
- Yuezhi Zhou
affiliations:
- Tsinghua University
- Beijing University of Posts and Telecommunications
- OpenBMB
arxiv_id: '2608.19181'
url: https://arxiv.org/abs/2608.19181
pdf_url: https://arxiv.org/pdf/2608.19181
published: '2026-08-19'
collected: '2026-08-20'
category: Training
direction: LLM蒸馏 · 长上下文推理优化
tags:
- On-Policy Distillation
- Long-Context Reasoning
- Knowledge Distillation
- LLM Training
- GC-OPD
one_liner: 通过分组残差校准和相对优势信用分配解决长上下文OPD中教师与验证器的偏好冲突
practical_value: '- 落地LLM Agent长上下文任务（如电商长文档属性抽取、用户长会话意图理解）的小模型蒸馏时，可直接复用GC-OPD框架，在保留原有token级蒸馏信号的同时接入业务自定义验证器奖励，无额外前向传播开销

  - 已使用On-Policy蒸馏做小模型落地的业务，可快速叠加RACA信用分配机制，将全局业务奖励按token相对OPD优势分配，效果优于均匀分配，且不需要额外标注成本

  - 长上下文生成式推荐场景（如基于用户30天浏览历史的个性化商品列表生成），可参考分组归一化残差思路，平衡教师模型的语言偏好和业务验证器的效果偏好，避免生成通顺但推荐准确率低的结果'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
长上下文任务中，传统On-Policy Distillation（OPD）依赖token级教师信号，容易偏好局部通顺但全局不符合任务要求的响应（如遗漏长文本中分散的证据、违反全局约束）。实验观测到两者的偏好冲突随上下文长度提升显著加剧：32-64K长度下，教师OPD分数与任务验证器奖励的排序不一致率可达60%以上，导致蒸馏得到的小模型长上下文推理性能达不到预期。
### 方法关键点
- 提出GC-OPD框架：对每个rollout组内的验证器奖励和轨迹级OPD分数分别做z-score归一化，计算两者差值作为有符号的教师-验证器不一致残差，仅对偏好冲突的部分做校准，完整保留原有蒸馏信号
- 相对优势信用分配（RACA）：将轨迹级残差按每个token的相对OPD优势分配到token层面，OPD优势越高的token分配的校准权重越大，不需要额外step级标注或辅助采样
- 工程轻量化：兼容二进制和分级奖励，无需跨任务校准，仅增加分组聚合、归一化和elementwise变换，无额外模型前向传播开销
### 关键实验
基于9.5K条32K以内的长上下文训练数据，用Qwen3-4B、Qwen3-8B做学生模型，Qwen3-30B做教师模型，在5个长上下文基准上测试：相比官方原始checkpoint，GC-OPD将4B模型平均分从29.08提升到40.47，8B模型从35.12提升到44.65；相比 vanilla OPD，4B提升1.16、8B提升1.09，效果优于ExOPD、Uni-OPD、FiRe-OPD等现有OPD变种。消融实验显示，残差校准比直接加验证器奖励多提0.46，RACA比均匀分配多提0.37。

长上下文蒸馏中不要盲目信任教师模型的token级偏好，用分组归一化的残差校准可以低成本融合业务验证信号，实现稳定效果增益
