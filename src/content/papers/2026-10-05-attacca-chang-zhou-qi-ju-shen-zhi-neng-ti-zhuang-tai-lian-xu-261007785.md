---
title: 'Attacca: Goal-Directed Control under State Continuity for Long-Horizon Embodied
  Agents'
title_zh: Attacca：长周期具身智能体状态连续场景下的目标导向控制方法
authors:
- Gyusik Seo
- Jaehong Yoon
affiliations:
- Nanyang Technological University, Singapore
arxiv_id: '2610.07785'
url: https://arxiv.org/abs/2610.07785
pdf_url: https://arxiv.org/pdf/2610.07785
published: '2026-10-05'
collected: '2026-10-07'
category: Agent
direction: 具身Agent长序列任务控制优化
tags:
- Embodied Agent
- Goal-Conditioned Policy
- Long-Horizon Task
- Visual Grounding
- Behavior Cloning
one_liner: 提出融合三类核心设计的具身Agent控制框架，大幅提升长序列任务的跨场景成功率
practical_value: '- 电商导购、服务类多轮交互Agent可参考**上下文解耦目标采样**思路：训练时将目标参考与当前交互场景解耦，避免策略依赖场景上下文shortcut，提升跨场景需求承接的泛化能力

  - 推荐系统用户长路径转化建模可复用**阶段显式建模**设计：将用户从种草、加购到下单划分为不同阶段，新增轻量阶段预测头，通过FiLM层做阶段感知的排序策略调整，提升长路径转化效率

  - 多模态搜推的同款匹配任务可迁移**mask预测辅助监督+残差反馈**方案：新增目标物品mask预测辅助损失，将mask特征以残差方式接入主排序模型，提升视觉同款匹配的精度'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有具身Agent的目标条件策略大多在孤立交互场景训练，要求目标初始可见，无法适配长序列任务的状态连续性：前序任务结束后Agent姿态、环境状态发生改变，下一个目标往往不在初始视野内，出现技能切换断层，导致长周期任务成功率极低。

### 方法关键点
- **上下文解耦目标采样**：训练时给每个演示轨迹配对来自其他场景的同类别带mask目标图片，移除目标和训练场景的姿态、场景对应关系，迫使策略仅通过目标外观匹配定位
- **目标条件grounding头**：新增预测当前帧目标mask的辅助头，用patch级二分类+Dice损失做监督，将mask特征残差接入Transformer输入，给动作预测提供目标位置/可见性信号
- **行为阶段条件调制**：显式建模搜索/接近/交互三个执行阶段，新增阶段预测头，通过FiLM层用预测的阶段特征调制动作头输入，让策略适配不同阶段的控制逻辑

### 关键结果
在Minecraft环境测试，基于1160条人类搜索-交互全流程演示训练，对比STEVE-1、ROCKET-2等7个基线：短周期任务（挖矿、狩猎、放置）成功率39.0%~47.5%，比最优基线高1.7~2.4倍；长周期任务链（钻石镐、喂狼、下界传送门）完成率54%、30%、28%，最高比基线提升7倍。

### 核心结论
长序列任务的性能瓶颈往往不是单技能精度，而是技能切换时的状态衔接断层，显式建模目标定位+阶段切换能大幅降低衔接损耗。
