---
title: 'QuoteBench: How Matched Scores Can Hide Command-Path Failures'
title_zh: QuoteBench：匹配分数如何掩盖命令执行路径故障
authors:
- Shangao Li
- Yao Zhang
- Volker Tresp
- Yuanyuan Yang
affiliations:
- Stony Brook University
- LMU Munich
- Munich Center for Machine Learning
arxiv_id: '2608.13547'
url: https://arxiv.org/abs/2608.13547
pdf_url: https://arxiv.org/pdf/2608.13547
published: '2026-08-13'
collected: '2026-08-14'
category: Agent
direction: Agent · 命令执行可靠性评测
tags:
- Agent
- Benchmark
- LLM
- Tool Use
- Command Execution
one_liner: 提出QuoteBench基准，可拆解LLM命令Agent的匹配得分，揭示执行路径对性能与排名的影响
practical_value: '- 做工具调用Agent时，不能只看端到端成功率，要单独校验LLM生成的命令/参数在实际传输链路（比如容器/远程调用/JSON序列化）下的正确性，避免中间层转义/解析带来的隐性故障

  - 部署跨环境执行的Agent（比如远程操作服务器、调用容器内命令）时，优先在接口层做统一转义，或者将命令写入临时脚本执行，可100%消除本文观测到的传输损失

  - 做Agent评测时，必须明确披露生成合约、执行环境、校验逻辑，不同链路下的模型排名不具备通用性，避免盲目选择SOTA模型

  - 若Agent需要适配不同执行链路，可在prompt中明确告知执行边界规则，能力较强的LLM可自动适配，最多可恢复60%+的传输损失'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前LLM命令生成Agent的评测仅关注端到端匹配得分，无法区分是命令生成错误还是执行链路中的转义/解析故障，这类隐性故障会导致任务失败、重试成本升高，甚至引发安全问题，但现有基准无法隔离这类边界问题。
### 方法关键点
- 构建QuoteBench基准，包含14个操作族共56个单步Bash任务，覆盖转义符、特殊文件名、多文本、远程调用模拟等高危场景，采用最终状态严格校验，不依赖程序退出码
- 采用2×2交叉设计，独立控制生成合约（原始/边界披露）和执行传输（直接/嵌套解析），通过固定回复重放的方式，将匹配得分拆解为传输损失和合约补偿两个独立分量
### 关键结果
在8组同窗口配置下，固定原始回复添加一层双引号解析，成功率下降55.4~73.2个百分点；给模型披露执行边界后，6组配置可恢复30.4~60.7个百分点的损失；仅3个模型在最优配置下达到100%通过率，其余模型得分在14.3%~98.2%区间，不同执行路径下的模型排名出现显著反转。
### 最值得记住的一句话
命令执行接口是Agent系统的核心组成部分，而非中立的管道，评测与部署都必须明确全链路的生成规则与执行环境。
