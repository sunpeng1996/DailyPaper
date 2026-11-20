---
title: 'CompoundingKernel: Self-Improving from Zero to First'
title_zh: CompoundingKernel：从零到榜首的自优化GPU内核生成Agent系统
authors:
- Qian Qu
- Hongyang Wang
- Wenbo Chen
- Yichuan Li
- Jingguo Liu
- Xian Li
- Xuan Wang
- Ruochen Wen
- Leo Fan
- Yiming Yan
affiliations:
- Amazon
arxiv_id: '2611.19230'
url: https://arxiv.org/abs/2611.19230
pdf_url: https://arxiv.org/pdf/2611.19230
published: '2026-11-13'
collected: '2026-11-20'
category: Agent
direction: Agent 多智体自优化代码生成
tags:
- MultiAgent
- SelfImproving
- GPUKernel
- CodeGeneration
- LLM
one_liner: 构建无参考内核的自优化多Agent系统，登顶SOL-ExecBench三大榜单，生成内核比基准快4.4倍
practical_value: '- 多Agent架构可直接复用：控制器+并行子Agent+外部无状态存档的分层设计，可迁移到推荐系统特征迭代、排序策略调优、LLM文案生成等需要持续试错的场景，热重启不丢失历史进度，降低迭代成本

  - 系统瓶颈优化思路：优先优化评测/反馈链路的速度、降低锁/排队开销，而非盲目增加Agent数量，该结论可直接应用于电商大促时的多候选内容生成、A/B测试链路优化，投入产出比更高

  - 迭代策略优化：不要只基于当前最优结果迭代，保留暂时性能落后的中间结果作为垫脚石，可迁移到召回/排序策略的多路径迭代，避免陷入局部最优

  - 奖励黑客防控：将正确性、合规性校验完全放在Agent外部，禁止Agent接触官方/真实业务指标，可应用于营销素材生成、推荐理由生成等场景，避免生成违规或作弊内容'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
GPU新硬件迭代速度远快于算子库适配速度，手动编写高性能内核门槛高、周期长；现有AI生成内核的方案大多依赖参考代码或官方评分，无法冷启动自优化，且普遍存在奖励黑客（作弊获取高评分）问题，难以落地到真实生产。
### 方法关键点
- 四层嵌套循环架构：子Agent负责单版本内核编写、编译、测速；LLM控制器基于历史存档选择优化父节点或开启新设计；辅助Agent负责工具链迭代，热重启不修改存档；人工仅负责最终提交决策
- 外部共享只读存档：所有正确内核及血统存储在SQLite数据库，Agent无状态，热重启后直接读取存档继续迭代，历史尝试永不丢失
- 全外部校验机制：正确性、性能、合规性校验完全在LLM外部执行，官方评分完全不进入搜索环路，从根源避免奖励黑客
- 多路径迭代规则：允许基于性能暂时落后的内核优化，将次优结果作为后续突破的垫脚石
### 关键结果
在NVIDIA B200的SOL-ExecBench基准测试上冷启动（无任何参考内核）：
- 登顶L1、L2、Quantization三个公开榜单，235个问题的内核全部通过官方正确性校验
- 209个公开问题的内核几何平均速度是PyTorch基准的4.4倍，中位数3.78倍，最高可达1062倍
- 同等耗时下，LLM控制器在38个问题中赢过编码实现的UCB树搜索35个，正确尝试数是后者的2.4倍
- 一次热重启优化将评测吞吐量提升3.6倍，GPU锁时间降低71%
### 核心结论
自优化Agent系统的规模瓶颈是可靠反馈的速率，而非Agent的数量，更多有效试错比额外的先验指导收益更高
