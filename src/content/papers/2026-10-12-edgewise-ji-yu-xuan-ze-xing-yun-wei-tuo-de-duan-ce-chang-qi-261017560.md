---
title: 'EdgeWise: Bringing Long-Horizon Agents to the Edge via Selective Cloud Delegation'
title_zh: EdgeWise：基于选择性云委托的端侧长周期Agent部署框架
authors:
- Zeru Shi
- Jindong Jiang
- Ryo Hachiuma
- Yonggan Fu
- Byung-Kwan Lee
- Peter Belcak
- Saurav Muralidharan
- Ayush Agarwal
- Ruixiang Tang
- Ambrish Dantrey
affiliations:
- NVIDIA
- Rutgers University
arxiv_id: '2610.17560'
url: https://arxiv.org/abs/2610.17560
pdf_url: https://arxiv.org/pdf/2610.17560
published: '2026-10-12'
collected: '2026-10-16'
category: Agent
direction: Agent 端云协作推理成本优化
tags:
- Agent
- SLM-LLM Collaboration
- Edge Computing
- Reinforcement Learning
- Inference Optimization
one_liner: 提出端侧SLM为主、按需委托云LLM的Agent协作框架，降本最高62%且性能持平纯云LLM
practical_value: '- 可复用「关键步骤识别+大小模型协作」思路，在电商推荐Agent、商品文案生成、复杂用户query理解等场景，简单步骤用本地SLM处理，高价值复杂步骤调用云LLM，大幅降低推理成本

  - 可直接复用两种委托机制：训练免版的外部轻量Judge识别高价值步骤，或是通过带细粒度credit assignment的RL让SLM学会自我委托，推理无需额外路由模型，降低架构复杂度

  - 委托上下文策略可直接复用：优先传全量历史保证云LLM效果，预算有限时剔除SLM推理过程仅传交互数据，灵活平衡效果与成本

  - 可通过调整委托阈值适配不同成本预算：比如大促高峰期提高阈值减少云调用，低峰期降低阈值保证服务效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长周期Agent任务全链路调用云大模型推理成本极高，但大部分中间步骤复杂度低，完全可由端侧小模型独立处理。现有模型路由方法多针对单Query或简单多跳任务，依赖额外预定义模型池的路由模块，在长周期Agent场景泛化性差，也无法适配端云协作的部署架构。
### 方法关键点
- 核心架构：端侧部署SLM作为主执行器，全流程处理环境交互，仅将少量关键步骤委托给云LLM执行
- 两种委托机制：训练免版的外部轻量Judge基于步骤类型（Write/Edit、复杂Read/Search等）识别高价值步骤；或是通过两阶段训练（SFT教授委托格式+带细粒度credit assignment的RL优化委托决策）让SLM学会自我委托，推理阶段无需额外路由模型
- 可通过调整委托阈值灵活控制云调用频率，适配不同成本预算
- 上下文策略：委托云LLM时优先传输全量历史保证效果，预算有限时可剔除SLM推理过程仅传输交互数据，平衡效果与成本
### 关键实验结果
在SWE-Rebench、Terminal-Bench 2.1两个长周期编码Agent基准上，对比纯云LLM、随机委托、MTRouter等基线，自我委托策略在性能持平甚至优于纯云LLM的前提下，SWE-Rebench降本最高62%，Terminal-Bench 2.1降本最高34%，在端侧设备DGX Spark上真实部署同样实现约50%的推理成本下降。

**最值得记住的结论**：长周期Agent任务中云大模型的价值仅集中在少量关键步骤，针对性分配算力而非全链路使用大模型，是兼顾效果与成本的核心思路。
