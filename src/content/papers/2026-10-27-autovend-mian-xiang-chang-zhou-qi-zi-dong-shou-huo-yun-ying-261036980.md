---
title: 'AutoVend: Benchmarking LLM Agents on Long-Horizon Autonomous Vending Operations'
title_zh: AutoVend：面向长周期自动售货运营的LLM Agent基准测试
authors:
- Qiming Shi
- Yikun Li
- Beidi Luan
- Rui Sun
- Sinuo Wang
- Delin Wang
- Yan Ma
- Jing Li
- Daxin Jiang
- Zuo Bai
affiliations:
- StepFun
- Zhejiang University
- Xi'an Jiaotong-Liverpool University
- University of Adelaide
- Renmin University of China
arxiv_id: '2610.36980'
url: https://arxiv.org/abs/2610.36980
pdf_url: https://arxiv.org/pdf/2610.36980
published: '2026-10-27'
collected: '2026-11-10'
category: Agent
direction: Agent 分布式零售运营能力评测
tags:
- LLM Agent
- Benchmark
- Autonomous Retail
- Long-Horizon Planning
- O2O Commerce
one_liner: 构建覆盖20台多场景售货机的180天模拟基准，评测LLM Agent的分布式零售运营能力
practical_value: '- 做O2O/线下零售Agent的团队可直接复用AutoVend的模拟器框架，尤其是多站点共享库存、补货lead time、执行成本的建模逻辑，无需从零搭建仿真环境

  - 电商多仓调度/多门店运营的Agent设计可规避论文暴露的典型失败模式：前置校验商品级库存可用性、批量合并线下执行动作降低成本、将反馈固化为通用策略而非单次临时修复

  - 投入Agent到生产前可参考论文的评测体系：除最终收益外，需同步评估API效率、策略稳定性、单指标优化与整体收益的对齐度，避免局部最优'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有卖方Agent评测多聚焦单一线上门店或单个线下点位，未覆盖O2O场景下多异质站点共享库存、线下补货有成本/延迟、长周期决策累计影响收益的核心痛点，无法评估Agent跨站点资源协调、物理执行规划、持续策略迭代的复合能力。

### 方法关键点
- 搭建180天仿真运营环境：单Agent管理5类场景共20台售货机，共享统一仓库，真实建模采购3天提前期、单台机器单次补货35元费用、库存过期罚款、仓储/机器固定租金等约束
- 需求模型基于真实6个月22万条售货机订单校准，覆盖不同站点的品类偏好、价格弹性、节假日/天气响应，持外测试WAPE达0.473，优于历史均值基准
- 提供18个MCP工具覆盖远程运营、物理执行、持久化记忆三类操作，评测指标包含终端净资产、品类匹配度、库存浪费率、API效率等多维度

### 关键结果
- 评测5款主流LLM Agent，仅GPT-6.1 Sol终端净资产达30.94万CNY，超过规则基线的21.10万CNY，其余4款模型均弱于规则基线
- 模型收益与API效率排名完全分离：DeepSeek V4.1 Flash API效率是GPT的27倍，每美元API投入可带来3.1万CNY的净资产增长
- 73%的Agent执行中存在局部指标优化未转化为整体收益的问题，核心失败模式包括库存校验缺失、线下执行动作碎片化、反馈未固化为长期策略

### 核心结论
长周期零售运营中，局部运营指标的优化不一定能转化为整体经济收益，必须同时平衡库存成本、执行成本和需求匹配的多重约束
