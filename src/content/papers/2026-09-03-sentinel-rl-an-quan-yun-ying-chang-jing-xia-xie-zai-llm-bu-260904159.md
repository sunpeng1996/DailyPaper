---
title: 'SENTINEL-RL: Offloading Topological Reasoning from LLM Agents in the Security
  Operations Center'
title_zh: SENTINEL-RL：安全运营场景下卸载LLM Agent拓扑推理的架构
authors:
- Uday Vallabhaneni
- Cassie L. Cagwin
- David J. Wild
affiliations:
- Indiana University Bloomington
arxiv_id: '2609.04159'
url: https://arxiv.org/abs/2609.04159
pdf_url: https://arxiv.org/pdf/2609.04159
published: '2026-09-03'
collected: '2026-09-04'
category: Agent
direction: 安全运营Agent 神经符号混合架构
tags:
- LLM Agent
- Reinforcement Learning
- Graph Neural Network
- Neuro-symbolic
- Security Operation
one_liner: 提出拆分拓扑与语义推理的SOC Agent架构，用HetGAT+PPO做决策，LLM仅负责生成可读报告
practical_value: '- 复杂决策场景可做LLM与专业推理模块拆分：把需要严谨规则的高风险决策（如推荐权益发放、广告投放阈值调整）交给专用GNN/RL模块，LLM仅承担语义理解、话术生成、报告输出工作，既降低
  hallucination 风险又节省上下文开销

  - 大规模图数据并行写入可复用两阶段CREATE trick：先顺序写入所有唯一节点再并行写入边，解决热点节点锁死问题，可直接用在电商用户行为图、商品关联图等大规模图数据的入库场景

  - Agent落地可复用三层权限分级框架：读操作自动执行、可逆操作需内部校验、高风险操作强制人工审核，可直接迁移到电商运营Agent、广告投放Agent的权限管控，避免不可挽回的业务损失

  - 低延迟在线系统可复用锚点节点部署模式：把延迟敏感的核心服务（如推理服务、调度模块）集中部署在同一物理节点，仅将批量计算任务做分布式调度，大幅降低跨节点通信延迟，提升系统稳定性'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前SOC场景下直接用LLM Agent做自主分析存在两个核心缺陷：一是LLM上下文窗口无法容纳企业级万级主机、百万级连接的认证拓扑图，信息不足会导致决策错误；二是LLM开放生成的响应无拓扑合规性保障，误操作会引发业务中断风险，现有方案既不可靠也无法满足企业级部署要求。

### 方法关键点
- 架构做四层拆分：数据平面用Neo4j存储实时网络拓扑图，战略平面用HetGAT把2跳邻域子图编码为64维固定向量，再用PPO策略输出5种受限的调查/处置动作，LLM仅负责把策略输出转换为分析师可读的叙事报告，同时加Critic模块校验证据充分性
- 工程优化：两阶段CREATE图入库模式，先顺序写入所有唯一节点再并行写入边，解决热点节点锁死问题；HPC锚点节点部署，核心服务集中在同一物理节点避免跨节点通信延迟
- 安全管控：三层权限分级，只读操作自动执行、可逆操作需Critic校验、高风险操作强制人工审核，所有操作留痕满足合规要求

### 关键结果
在LANL网络安全数据集和印第安纳大学Quartz HPC集群验证：24M边的认证子图入库仅需14.2分钟，比传统MERGE模式吞吐量提升24倍；滑动窗口告警触发99分位延迟≤2.5秒，端到端检测→推荐全流程中位数耗时6.3秒；PPO训练200轮收敛，红队事件检测precision 0.91、recall 0.87，F1领先同类型图检测方案。

**最值得记住的一句话**：不要强迫LLM处理所有任务，把它限制在擅长的语义工作上，将需要严谨约束、复杂拓扑/逻辑推理的决策交给专用模块，是Agent落地的核心可行路径。
