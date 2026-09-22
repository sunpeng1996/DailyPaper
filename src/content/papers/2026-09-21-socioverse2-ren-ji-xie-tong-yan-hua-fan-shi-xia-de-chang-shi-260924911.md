---
title: 'SocioVerse2: A Longitudinal Dynamic Social Simulation Framework under a Human-AI
  Co-evolutionary Paradigm'
title_zh: SocioVerse2：人机协同演化范式下的长时序动态社会模拟框架
authors:
- Xinnong Zhang
- Jiayu Lin
- Jia Wang
- Yixu Huang
- Xinyi Mou
- Yingqian Wu
- Jingcong Liang
- Shijun Lei
- Jianing Shi
- Guanying Li
affiliations:
- 复旦大学
- 上海创新研究院
- 伦敦国王学院
- 同济大学
- 西北工业大学
arxiv_id: '2609.24911'
url: https://arxiv.org/abs/2609.24911
pdf_url: https://arxiv.org/pdf/2609.24911
published: '2026-09-21'
collected: '2026-09-22'
category: MultiAgent
direction: 多智能体社会模拟 · 人机协同演化
tags:
- MultiAgent Simulation
- Human-AI Collaboration
- Counterfactual Inference
- LLM Agent
- Social Simulation
one_liner: 提出双循环人机协同社会模拟框架，支持反事实干预、人在回路控制与多场景仿真
practical_value: '- 可复用回放式反事实分支设计：电商/营销场景下做不同活动方案的前置仿真时，无需全量重跑历史，仅从干预步骤分叉计算，算力成本降低60%以上，可快速对比多组方案的效果差异

  - 多源persona池的MCP协议可直接迁移：推荐系统做目标客群的行为模拟时，可复用跨池路由、IPF分布对齐方法，快速生成符合真实人口属性的用户画像池，替代小流量AB测试做前置验证

  - 双循环人在回路架构可借鉴到Agent推荐系统：将算法工程师的干预与Agent自主运行结合，既保留Agent的自动化能力，又可随时修正Agent漂移问题，提升推荐策略迭代的可控性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM驱动的社会模拟平台存在两类缺陷：固定沙箱类平台缺乏动态干预能力，无法开展反事实实验；全自治Agent平台容易脱离预设目标生成不可靠结果，且无法满足科研/产业场景对仿真过程的可控性要求，此前的SocioVerse1.0仅支持横截面人群对齐，不支持长时序演化与干预。
### 方法关键点
- 双循环架构：纵向仿真循环实现长时序环境与用户行为的迭代演化，支持在任意步骤插入干预生成反事实分支，通过回放父分支历史避免重复计算；可控研究循环支持对人口、环境、行为函数、参数的任意编辑，生成不同版本的仿真实验，全版本可追溯可复现。
- 标准化Agent基础设施：提供人口MCP服务，整合5个千万级真实用户/合成persona池，支持按目标人口分布通过IPF算法采样对齐；提供事件MCP服务，接入21个真实世界信号源，支持时点访问保证，避免仿真时泄露未来数据。
- 多模式行为函数：支持规则、LLM、RL、混合四种行为决策模式，可根据场景需求平衡仿真效率与精度。
### 关键结果数字
在3类场景7个案例完成验证：1）经典ABM模型复现准确率≥95%；2）政策仿真（芝加哥种族隔离、药品采购）结果与真实统计数据偏差<3%；3）宏观指数临近预测（消费者信心指数、PMI、德国乘用车市场份额）准确率比纯时间序列baseline高12~18个百分点，可超越模型知识cutoff生成预测结果。
### 核心结论
人机协同而非纯Agent自治，才是下一代高可信度社会/产业仿真的核心范式。
