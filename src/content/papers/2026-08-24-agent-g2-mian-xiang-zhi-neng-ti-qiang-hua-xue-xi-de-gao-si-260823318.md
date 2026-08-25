---
title: 'Agent-G$^2$: Gaussian Guidance for Agentic Reinforcement Learning'
title_zh: Agent-G²：面向智能体强化学习的高斯引导框架
authors:
- Zixuan Wang
- Yanrui Miao
- Zhengxi Lu
- Teng Pan
- Yiwen Qiu
- Hongxing Li
- Peng Qiu
- Ruiqing Zhang
- Yongliang Shen
affiliations:
- Zhejiang University
- Baidu Inc.
- Shandong University
arxiv_id: '2608.23318'
url: https://arxiv.org/abs/2608.23318
pdf_url: https://arxiv.org/pdf/2608.23318
published: '2026-08-24'
collected: '2026-08-25'
category: Agent
direction: LLM Agent 强化学习训练优化
tags:
- LLM Agent
- Reinforcement Learning
- GRPO
- Hint-based RL
- Long-horizon Task
one_liner: 用动态高斯分布采样引导深度，零额外探针开销提升长序列LLM Agent RL训练效果
practical_value: '- 电商导购/多轮搜索Agent训练可复用该高斯采样引导策略，替代固定步长hint调度，无需额外探针rollout即可缓解奖励稀疏问题，提升长路径任务（如多轮商品筛选、下单引导）的完成率

  - 可借鉴全局基线+任务难度分簇的统计更新逻辑，给推荐系统多场景/多难度训练任务做自适应课程学习调度，无需额外标注即可匹配不同难度样本的训练节奏

  - 基于GRPO训练Agent时，可复用前缀SFT+GRPO联合损失的设计，稳定训练收敛，避免优势崩塌问题'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
长序列LLM Agent强化学习普遍存在奖励稀疏问题，hint-based RL通过注入专家轨迹前缀缓解该问题，但现有方案要么采用全局固定引导深度忽略任务异质性，要么需额外探针rollout估算单任务最优深度，训练成本高、适配性差，且均假设最优深度是单一确定性值，不符合实际训练信号分布。
### 方法关键点
- 验证引导深度的邻域结构：有效深度是围绕最优值的高斯分布带而非单点，R²拟合度达0.92
- 采用离线分簇（按专家轨迹长度划分难度）+在线更新架构：全局基线μ随批量成功率动态调整，分簇维护EMA平滑的成功率Ak和方差Vk，生成单任务的高斯分布参数
- 单任务从高斯分布采样引导深度，复用GRPO已有rollout统计更新分布参数，零额外探针开销
- 训练损失结合GRPO RL损失和前缀SFT辅助损失，稳定收敛
### 关键实验
在ALFWorld、WebShop两个长序列Agent基准测试，基模型采用Qwen2.5-1.5B/7B-Instruct，对比10+种hint-based、无hint、Aux-RL基线：ALFWorld上1.5B版本成功率达95.3%，7B版本达98.4%，比最强基线高2.3~7.4个点，rollout成本仅为探针式方案的1/3；WebShop上两个版本均获92.3 reward score，购买成功率分别达78.9%、84.4%。
> 引导深度的核心是覆盖有效邻域而非精准定位单点，合理的调度设计可替代模型规模缩放降低训练成本。
