---
title: 'Qwen-CUA: Native Computer Use for (almost) Everything'
title_zh: Qwen-CUA：基于原生键鼠操作的通用计算机使用Agent
authors:
- Dunjie Lu
- Shuai Bai
- Tianyi Bai
- Sicheng Fan
- Chang Gao
- Jian Guan
- Feng Hu
- Mianqiu Huang
- Xingyang Huang
- Yizhen Jiang
affiliations:
- Qwen Team
- XLANG Lab
- Alibaba Cloud
arxiv_id: '2608.02352'
url: https://arxiv.org/abs/2608.02352
pdf_url: https://arxiv.org/pdf/2608.02352
published: '2026-08-03'
collected: '2026-08-04'
category: Agent
direction: 计算机使用Agent · 原生视觉交互优化
tags:
- Computer Use Agent
- MoE
- Reinforcement Learning
- Multimodal Agent
- GUI Interaction
one_liner: 基于Qwen MoE基座的纯视觉原生计算机使用Agent，性能比肩头部闭源系统
practical_value: '- 长上下文视觉历史的块式折叠方案可直接复用在多轮交互Agent的KV cache优化上，按固定步长折叠旧视觉输入，既保留最近证据又提升前缀缓存命中率，降低推理成本

  - 迭代式训练的任务校准策略可迁移到Agent微调流程：每次迭代用当前模型筛选难度适中的RL任务（既不太难也不已经饱和），集中优化提升效率

  - 纯原生视觉交互+工具调用的混合架构可复用在电商运营Agent场景：原生操作适配无API的商家后台/第三方平台，搭配脚本工具提升批量操作效率

  - 可验证奖励的RL训练范式可迁移到业务Agent的效果优化：用最终状态的可执行校验替代人工标注step级奖励，降低训练数据成本'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Agent大多依赖API、DOM树、无障碍元数据等结构化环境信息，无法覆盖无公开接口的桌面软件、legacy系统、动态网站、专业工具等场景，而仅通过截图感知、键鼠操作的原生计算机使用模式可以操作所有人类可访问的软件，但面临长交互流程状态难追踪、交互数据采集成本高、奖励稀疏验证难等痛点。
### 方法关键点
- 基座采用397B-A17B MoE架构，仅输入屏幕截图，输出原生键鼠操作指令，不依赖任何额外结构化环境信息
- 长上下文管理：保留最近20张活跃截图，超出后按10张为块将旧截图折叠为文本占位符，既保留近期视觉证据，又稳定prompt前缀提升KV cache复用率；训练时通过轨迹切片对齐推理逻辑，无需额外摘要模型
- 训练基建：搭建近10万vCPU、支持数万并发环境的云调度集群，构建4万+可验证任务，覆盖日常/专业软件、长流程、用户交互等场景，搭配个性化桌面的专家演示轨迹
- 训练范式：采用基于最终状态可验证奖励的SAPO强化学习，迭代式更新训练数据和RL任务分布，每次迭代用当前模型筛选难度适中的任务，集中优化提升训练效率
### 关键结果
在8个主流计算机使用基准上对比Qwen3.7、GPT-5.5、Claude Opus 4.8：Qwen-CUA在OSWorld-Verified上得分86.2，超过Qwen3.7的73.3、GPT-5.5的78.7和Opus 4.8的83.4；OSWorld 2.0二元/部分完成率达18.5/48.4，远高于Qwen3.7的2.5/22.5；RedTeamCUA攻击成功率较Qwen3.7从36.6降至16.4，同时任务成功率提升；扩容到万亿参数的Qwen-CUA-Max进一步将OSWorld-Verified得分提升至87.6。
### 核心结论
原生计算机使用可以作为通用Agent的基础交互层，搭配结构化工具、脚本等可以在场景覆盖度和执行效率上达到更优平衡。
