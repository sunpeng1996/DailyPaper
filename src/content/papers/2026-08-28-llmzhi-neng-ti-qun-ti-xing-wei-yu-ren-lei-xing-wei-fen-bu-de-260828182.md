---
title: Benchmarking large language model agent societies against human behavioural
  distributions
title_zh: LLM智能体群体行为与人类行为分布的基准评测
authors:
- Raad Bin Tareaf
affiliations:
- XU Exponential University of Applied Sciences, Germany
arxiv_id: '2608.28182'
url: https://arxiv.org/abs/2608.28182
pdf_url: https://arxiv.org/pdf/2608.28182
published: '2026-08-28'
collected: '2026-08-31'
category: Agent
direction: LLM多智能体社会模拟有效性评测
tags:
- LLM Agent
- Multi-agent Simulation
- Benchmark
- Behavioural Alignment
- Contamination Audit
one_liner: 推出开源SILICA基准，从三维度评测LLM多智能体群体行为与人类的匹配度
practical_value: '- 做电商用户群体仿真、消费行为推演时，可复用SILICA的扰动设计，校验Agent行为是否受prompt格式、选项顺序等无意义变量影响，避免仿真结果偏误

  - 多Agent协商场景（如商家议价、用户群体共识模拟）可借鉴污染审计思路，通过修改收益规则区分Agent是真的理解规则还是在复述训练集记忆脚本

  - 落地多Agent系统时优先选经过推理训练的模型，这类模型对规则变化的响应更符合实际激励要求，稳定性更高

  - 不要用单一模型的仿真结果做业务决策，不同模型行为异质性极高，同一规则下输出可能覆盖0-1全范围'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM多智能体被广泛用于社会仿真、用户行为推演、政策效果模拟，但业界一直缺乏统一工具校验三类核心问题：智能体行为是否与真实人类对齐、仿真结果是否受实验装置无关细节干扰、观察到的群体动态是真实交互还是模型复述训练集中的实验脚本。
### 方法关键点
- 构建SILICA开源评测框架，包含5个有成熟人类行为锚点的经典博弈环境（重复囚徒困境、带惩罚公共品博弈、议价博弈、11-20金钱请求博弈、命名博弈）
- 设计两层扰动库：表征层扰动仅修改信息呈现形式（如选项顺序、persona排版）不改变规则，设计层扰动修改Agent输入信息不改变收益
- 设计污染审计梯度，修改收益规则让训练集中记忆的标准答案不再最优，区分行为来源是记忆还是推理
- 测试12个开源LLM，所有实验在单张消费级GPU上运行，共9115次有效仿真
### 关键结果
- 保真度仅在初始阶段匹配：11个模型中8个的首轮公共品贡献在人类等价区间内，无模型匹配终轮贡献或人类合作动态轨迹
- 鲁棒性存在明显缺陷：表征层扰动在8/71的对比中显著改变行为（如交换选项顺序让某模型合作率降58个百分点），设计层扰动在56/111的对比中改变行为
- 污染问题突出：仅1个经过推理训练的模型能将议价接受阈值设置到激励要求的位置，2个部分调整，2个反向调整，3个完全无稳定阈值
### 核心结论
当前LLM多智能体仅能复现人类交互的起点，无法复现交互发展的动态过程，其仿真结果仅可用于生成探索性假设，不能直接用于业务决策或效果预测
