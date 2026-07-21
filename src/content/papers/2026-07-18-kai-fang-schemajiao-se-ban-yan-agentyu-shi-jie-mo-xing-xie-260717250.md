---
title: 'EvolvingWorld: An Open-Schema Framework for Co-Evolving Role-Play Agents and
  World Model in Interactive Literary World'
title_zh: 开放Schema角色扮演Agent与世界模型协同演化框架EvolvingWorld
authors:
- Qing Zong
- Yue Guo
- Mengxin Yang
- Yiwen Guo
- Yangqiu Song
affiliations:
- Hong Kong University of Science and Technology
- LIGHTSPEED
- Huazhong University of Science and Technology
- Independent Researcher
arxiv_id: '2607.17250'
url: https://arxiv.org/abs/2607.17250
pdf_url: https://arxiv.org/pdf/2607.17250
published: '2026-07-18'
collected: '2026-07-21'
category: MultiAgent
direction: 多Agent世界模拟 · 开放Schema共演进
tags:
- Multi-Agent
- Open-Schema
- World Model
- Role-Play
- Long-Horizon Simulation
one_liner: 提出耦合开放Schema角色Agent与世界模型的长时序文学模拟框架，配套数据集与多维度评估体系
practical_value: '- 电商用户/商家动态画像建模可复用开放Schema+多时间尺度隐藏Tracker设计：无需预设固定画像字段，自动适配不同用户/商家的特征维度，弱信号先存入隐藏Tracker，累积到阈值再更新正式画像，避免短期行为导致的画像抖动

  - 多Agent互动场景（如直播虚拟主播与观众互动、虚拟社群运营）可参考7个可训练子任务的拆解逻辑，将长时序交互拆分为场景规划、互动生成、状态更新等独立子任务，降低端到端训练与调试难度

  - 长时序Agent/推荐系统的评估可借鉴轨迹级LLM-as-Judge评估方案，覆盖状态一致性、演化平滑度、环境感知等多维度，相比单次交互评估更能反映长期效果

  - 动态内容生成场景（如个性化互动广告、剧情类内容推荐）可复用世界模型分层状态设计，全局规则+场景/实体级状态分开维护，保证生成内容的前后一致性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有角色扮演Agent系统普遍依赖静态人设或固定Schema沙盒环境，无法支撑长时序模拟下角色与世界的协同演化，长序列运行时一致性快速下降，且难以适配多样化场景需求，缺乏通用的长时序多Agent模拟框架。
### 方法关键点
- 架构采用双耦合模块设计：开放Schema Character Agent支持多角色人设动态演化，引入隐藏Tracker存储弱演化信号，实现多时间尺度更新（情绪等短期特征快速调整，性格等长期特征需累积足够证据才更新）；LLM-based World Model维护全局、位置、实体三级开放Schema状态，自动驱动场景推进。
- 将长时序模拟流程拆解为7个可独立训练的子任务，覆盖场景初始化、交互生成、状态更新全链路，避免长序列任务梯度消失问题。
- 配套10维度20指标的轨迹级LLM-as-Judge评估体系，同时覆盖角色演化与世界状态维护的质量。
### 关键实验结果
基于57本公开书籍构建了138596条监督训练样本、222个测试快照，对比BookWorld、CoSER、Crab等主流基线：同基座下EvolvingWorld训练后比基线平均得分提升10~15分；15轮长时序模拟下，BookWorld的Profile演化平滑度下降12分，EvolvingWorld仅波动2分；32B参数训练版World Model得分超过Claude-4.6-Sonnet等闭源模型。
### 最值得记住的结论
长时序多Agent系统的核心竞争力不是单次交互的拟真度，而是角色与环境状态的耦合协同演化一致性
