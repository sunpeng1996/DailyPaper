---
title: Learning a patient world model for health system simulation in intensive care
title_zh: 面向重症监护医疗系统仿真的患者世界模型学习
authors:
- Yingtai Li
- Ruoyan Wang
- Yu Li
- Shaohua Kevin Zhou
affiliations:
- 中国科学技术大学生物医学工程学院
- 中科大苏州高等研究院MIRACLE实验室
- 中国医学科学院北京协和医学院群医学及公共卫生学院
- 北京公共卫生应急管理创新中心
- 呼吸健康与多发病国家重点实验室
arxiv_id: '2611.08392'
url: https://arxiv.org/abs/2611.08392
pdf_url: https://arxiv.org/pdf/2611.08392
published: '2026-11-05'
collected: '2026-11-08'
category: Other
direction: 世界模型 · 时序动态仿真与策略评估
tags:
- World Model
- Time Series
- Simulation
- Representation Learning
- Healthcare AI
one_liner: 基于长时序EHR训练通用患者世界模型，支持多场景ICU运营策略仿真无需重训
practical_value: '- 通用仿真底座架构可复用：核心模型一次训练冻结，仅新增场景适配层对接业务规则，避免多策略评估重复建模，可迁移到电商大促资源调度、仓配仿真、流量分配评估等场景

  - 时序行为建模思路可借鉴：摒弃短视的单状态马尔可夫假设，用长时序表征捕捉历史轨迹对未来需求的差异化影响，可优化用户复购预估、生命周期价值预测任务效果

  - 仿真验证框架可参考：从整体统计一致性、策略响应敏感性、微观个体合理性三个维度验证仿真效果，可用于搭建电商流量、库存、履约仿真系统的评估体系'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
传统医疗系统仿真方法为单一策略问题定制紧凑状态转移规则，忽略历史依赖动态，新场景需重新定义状态与转移逻辑，建模成本极高，无法支持多场景策略快速评估。
### 方法关键点
从长时序电子健康记录（EHR）学习通用患者世界模型，输出支持时间查询的患者轨迹统一表征；模型训练完成后冻结，仅通过轻量场景映射层对接ICU床位、护理资源、排队队列等业务规则，即可覆盖床位容量评估、护理调度、ICU转出能力评估等多类仿真任务。
### 关键结果数字
在MIMIC-IV数据集上，模型的整体床位占用率、策略响应效果与马尔可夫/半马尔可夫基准方法相当；对当前状态一致但历史轨迹不同的患者，可准确捕捉24h恢复率差异（预测-6.4pp vs 实际观测-6.7pp），该差异是传统紧凑状态模型完全无法识别的，会直接传导到护理需求、队列负担、床位使用率的仿真结果中。
