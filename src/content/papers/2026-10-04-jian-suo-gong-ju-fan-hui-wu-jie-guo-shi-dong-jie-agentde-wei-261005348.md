---
title: 'Search Engines Never Say No: How Frozen Agents React When the Retrieval Tool
  Refuses'
title_zh: 检索工具返回无结果时冻结Agent的行为表现研究
authors:
- Ramraj Chandradevan
- Sayontan Ghosh
- Vinoth Selvendran
arxiv_id: '2610.05348'
url: https://arxiv.org/abs/2610.05348
pdf_url: https://arxiv.org/pdf/2610.05348
published: '2026-10-04'
collected: '2026-10-06'
category: Agent
direction: Agent 检索工具交互优化
tags:
- Agent
- RAG
- Hallucination Mitigation
- Tool Calling
- Frozen LLM
one_liner: 检索工具侧加无结果拒绝提示，无需改动Agent/检索栈即可大幅降低合规Agent幻觉
practical_value: '- 电商/搜索Agent场景可直接在检索工具侧新增无结果拒绝逻辑，优先选择带指令的措辞（如"未找到可靠结果，请更换查询或返回未知"），对Qwen3、Claude
  Haiku这类合规Agent可降低84%的幻觉，且无需改动Agent和检索栈，落地成本极低

  - 针对不同大模型定制拒答引导策略：对Qwen3、Haiku等模型将拒答指令放在工具返回结果中效果最优，对Claude 5.5系列优先在system prompt中添加证据不足则返回未知的指令

  - 可复用收益-信号质量曲线评估自研无结果检测器的价值：在固定误拒率预算下，检测器召回率直接对应幻觉降低的收益，当前优化瓶颈在检测器而非Agent'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前检索工具无论索引是否存在答案都会返回top-k文本，冻结Agent（尤其是闭源API模型）无法识别无结果场景，极易产生幻觉；Agent侧训练拒答能力需要权重权限，检索栈全链路改造成本高，缺乏低成本通用解决方案。

### 方法关键点
- 构造索引漏洞测试集：257条NQ、300条HotpotQA问题，分别运行在含答案的完整索引和删除答案的漏洞索引下，确保无答案场景通过构造得到而非人工标注
- 设计5种拒绝返回措辞：空结果列表、仅NULL标记、带解释的NULL、带拒答指令的NULL、正常结果前加软警告，对比仅系统提示加拒答指令的基线
- 测试7种冻结Agent：Qwen3-8B/32B、Claude Haiku4.5、Sonnet5.5、Opus5.5、Search-R1，所有Agent均不做微调
- 提出收益-信号质量曲线，可基于检测器召回率和固定误拒率预算直接量化幻觉降低收益

### 关键结果
- 对Qwen3-8B/32B、Haiku4.5三类合规Agent，带解释的拒绝提示可将无答案场景下的拒答率从平均24.4%提升到83.7%，幻觉率下降84%，效果比仅系统提示加指令高51个百分点，且有答案场景的准确率和检索次数无变化
- 拒绝措辞效果排序：带指令的拒绝 > 带解释的拒绝 > 仅NULL标记≈空结果 > 软警告（几乎无效）
- 非合规Agent表现：Search-R1忽略拒绝并虚构检索结果，Claude 5.5系列优先从内存回答，对工具拒绝的响应差，但系统提示加指令可提升16个百分点的拒答率

### 核心结论
对可合规响应工具拒绝的Agent，检索工具侧加无结果提示是零训练成本、效果显著的幻觉 mitigation 方案，优化瓶颈在检索侧的无结果检测器而非Agent
