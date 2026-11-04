---
title: 'ToolSpace: Scaling Tool-Centric Environment Synthesis for Long-Horizon Agents'
title_zh: ToolSpace：面向长程智能体的工具中心化环境合成框架
authors:
- Guanting Dong
- Zhichao Sun
- Xinyu Yang
- Rui Wang
- Xin Deng
- Jiajie Jin
- Zhixiong Yang
- Junhao Huang
- Han Han
- Mingyu Ma
affiliations:
- Renmin University of China
- Fudan University
- Shanghai Jiao Tong University
arxiv_id: '2611.05036'
url: https://arxiv.org/abs/2611.05036
pdf_url: https://arxiv.org/pdf/2611.05036
published: '2026-11-02'
collected: '2026-11-04'
category: Agent
direction: Agent 长程工具调用训练数据合成
tags:
- Tool-Use Agent
- Long-Horizon Agent
- MCP
- Training Data Synthesis
- Environment Simulation
one_liner: 从真实工具执行轨迹构建可扩展组合图，低成本生成跨环境长程Agent训练样本并升级基准难度
practical_value: '- 搭建电商/运营类工具调用Agent的训练数据集时，优先从真实业务工具执行轨迹挖掘数据/状态/重试三类依赖，用确定性规则替代LLM判断，既保证工具组合逻辑的真实性，又降低数据生成成本

  - 跨业务系统（商品/订单/支付/客服）的工具调用任务合成可复用带回滚的状态感知随机游走方案，仅保留可从初始状态完整重放的样本，避免幻觉样本导致训练出的Agent落地时调用失败

  - 业务侧评估Agent工具调用能力时，可基于该框架升级现有测试基准，生成跨多系统的难例，快速定位Agent在长程复杂调用场景下的短板

  - 搭建Agent模拟训练环境时，仅为涉及状态修改的工具合成底层数据库，无状态/只读工具直接复用历史返回结果，可降低50%以上的环境合成成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有长程Agent环境合成均采用数据中心化范式：先构建数据库与场景，再衍生对应工具与任务，存在三大痛点：工具接口与真实业务接口不匹配、工具组合逻辑无实际执行依据、生成任务几乎不跨环境，导致训练出的Agent工具调用能力难以迁移到真实场景，也无法生成足够难度的长程跨环境训练/测试样本。
### 方法关键点
- 工具空间探索：从真实MCP服务执行轨迹、开源Agent语料的相邻调用中，用确定性规则挖掘三类边（数据依赖：前序输出作为后序输入；状态依赖：前序修改的对象被后序读写；重试依赖：前序调用失败后换工具成功），构建带权重的工具组合图，按连接密度聚类为环境，仅为包含状态修改操作的环境合成数据库，查询/无状态工具直接复用历史返回结果。
- 跨环境任务合成：在工具图上执行带回滚的状态感知随机游走，采样状态兼容的工具链，仅保留可从初始状态完整重放的链，反编译为不含工具名、调用顺序的自然语言任务，配套断言校验脚本。
### 关键实验
覆盖7个长程工具调用基准，Qwen3.6-35B-A3B平均得分从23.0提升至41.0（加RL后达43.2），GLM-5.2从44.6提升至56.6，性能追平Claude Opus 5；生成的AutomationBench Pro、τ³-Bench Banking Pro两个高难度基准，7个前沿模型得分最高下降38.2分；消融实验证明执行见证的边效果显著优于LLM判断的边，性能随数据、环境规模持续提升。
> 最值得记住的洞见：工具是Agent能力增长的原子单位，而非静态环境数据的附属品
