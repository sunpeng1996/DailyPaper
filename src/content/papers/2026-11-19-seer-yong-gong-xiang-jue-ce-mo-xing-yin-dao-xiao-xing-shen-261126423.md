---
title: 'Seer: Guiding Small Deep-Research Agents with Shared Decision Models'
title_zh: Seer：用共享决策模型引导小型深度研究Agent
authors:
- Yuhao Zhou
- Yang Zhou
- Yuanxi Li
- Jindi Lv
- Dan Si
- Qing Ye
- Jiancheng Lv
affiliations:
- Sichuan University
- University of Illinois at Urbana-Champaign
- Lenovo Group Limited
arxiv_id: '2611.26423'
url: https://arxiv.org/abs/2611.26423
pdf_url: https://arxiv.org/pdf/2611.26423
published: '2026-11-19'
collected: '2026-11-20'
category: Agent
direction: Agent推理优化 · 共享决策模型
tags:
- Small Agent
- On-device Agent
- Tool-use Agent
- Inference-time Optimization
- World Model
one_liner: 提出推理时框架Seer，复用共享决策模型提升小型研究Agent性能且不增加废弃候选的工具调用开销
practical_value: '- 端侧个性化推荐Agent/购物助手场景可复用离线训练的共享工具响应模拟器+价值估计器，无需为每个端侧小模型单独微调，大幅降低适配成本

  - 搜索推荐/广告场景工具调用（召回、商品详情查询、权益查询）成本高的场景，可借鉴候选动作模拟+预打分逻辑，仅执行Top1动作，废弃候选无需真实调用，大幅降低接口开销

  - 价值估计器训练可复用轨迹折扣终态奖励标注方法，无需复杂过程标注，仅用任务最终结果即可训练通用决策打分模型，适合多业务场景共享'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
端侧运行深度研究Agent面临算力/内存约束，小模型原生性能差，现有推理时优化要么需要针对特定模型微调，要么要真实执行废弃候选导致工具调用成本过高，无法跨不同Agent模型复用。

### 方法关键点
- 架构解耦：将Agent动作生成与工具响应预测、价值估计分离，两个共享决策模型（工具响应模拟器、价值估计器）离线训练后跨Agent复用，无需微调目标Agent
- 数据采集：通过蒙特卡洛分支采集多Agent多任务的真实交互轨迹，提取<调用-响应>对训练模拟器，用折扣终态正确性标注轨迹前缀训练价值估计器
- 推理逻辑：每轮Agent生成多个候选动作，模拟器预测各动作的工具响应，价值估计器打分想象轨迹，仅选最高价值的动作真实执行，保留真实响应更新历史

### 关键实验
在GAIA、BrowseComp等5个深度研究基准测试，对比Base Agent、BoN@4、AV@4等基线：Qwen3.5-4B的GAIA准确率从13.6%提升到41.7%，Qwen3.5-9B从22.3%提升到50.5%，工具调用量和Base Agent基本持平，性能收益覆盖4B到397B全尺寸模型。

最值得记住的结论：用额外本地推理成本换工具调用成本的节省，跨Agent复用的通用决策模型可以在不调整Agent本身的前提下大幅提升性能。
