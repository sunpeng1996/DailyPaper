---
title: Has GPT-6-Astra Achieved Embodied Intelligence?
title_zh: GPT-6-Astra具身智能能力评估与落地瓶颈分析
authors:
- SenseNova
- Joint Research Team
- Zhongang Cai
- Ziang Cao
- Tailai Chen
- Han Chong Chua
- Linjun Dai
- Hanming Deng
- Hokin Deng
- Haiwen Diao
affiliations:
- SenseNova 商汤联合研究团队
arxiv_id: '2610.22471'
url: https://arxiv.org/abs/2610.22471
pdf_url: https://arxiv.org/pdf/2610.22471
published: '2026-10-15'
collected: '2026-10-22'
category: Agent
direction: 具身Agent能力评估与架构优化
tags:
- Embodied AI
- LLM Agent
- In-Context Learning
- System 1-2
- Benchmark
one_liner: 大规模评估GPT-6-Astra跨12个具身基准的性能，明确其能力边界与落地瓶颈
practical_value: '- 可复用ICL知识包的6组件结构，在电商导购、客服Agent场景中，提前将商品信息、流程规则、故障处理方案封装为只读知识包，无需微调即可提升大模型任务完成率

  - 分层Agent架构可直接迁移到复杂推荐场景：高层LLM做用户意图理解、路径规划，低阶轻量化模型做点击预测、动作执行，搭配自适应动作块平衡效果与调用成本

  - 评估指标设计可借鉴下一代具身基准思路，业务侧评估Agent效果时需加入真实约束（如用户等待时长阈值、操作不可逆场景限制），避免理想环境下的性能虚高'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
现有具身智能领域长期采用单任务定制专项模型的范式，GPT-6-Astra这类通用大模型的具身能力边界、落地瓶颈尚未被系统量化，亟需统一的评估框架明确领域后续研发方向。
### 方法关键点
- 统一评估协议：允许模型通过ICL读取训练集演示，生成包含任务指引、动作参考、校验规则等6类组件的只读知识包，支持1~10倍官方步骤预算扩展，全程冻结模型权重
- 分层架构消融：对比System 2（GPT-6-Astra）与System 1（低阶机器人控制模型）的开/闭环协作模式，验证动作表征、自适应动作分块对性能与成本的影响
- 真实世界验证：在8种不同形态的机器人平台上开展零-shot部署测试，评估无域内演示、物理约束下的实际表现
- 下一代具身基准设计：提出任务源自真实用户需求、不提供域内演示、世界时钟随推理同步推进三大核心评估原则
### 关键结果
跨12个覆盖桌面操作、人形机器人、移动平台、灵巧手、导航的具身基准测试，1倍官方步骤预算下，GPT-6-Astra在LIBERO系列、SIMPLE等任务上成功率接近饱和，超过现有SOTA最高近1倍；10倍预算下RoboDojo成功率从27.6%提升至81.9%，DexJoCo达87.3%。真实世界部署中刚性物体抓取成功率达17/18，但精密接触、长horizon任务成功率不足30%。
### 核心结论
GPT-6-Astra已跨过具身能力门槛，但要实现规模化落地，仍需解决ICL跨任务泛化差、推理成本过高、物理状态校验不准、不可逆故障难以恢复、长周期进度易丢失五大核心问题。
