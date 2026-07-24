---
title: 'Tencent WorkBuddy Bench: A Multi-Domain Coding-Agent Benchmark with Contamination-Resistant
  Task Construction'
title_zh: 腾讯WorkBuddy Bench：多领域编码Agent抗污染评估基准
authors:
- Tencent WorkBuddy Bench Team
- Siqi Cai
- Shaopeng Chen
- Xiang Fei
- Yong Mao
- Zihan Xu
- Zhiheng Lyu
- Zhijian Shao
- Yuchen Shi
- Shuwen Zhang
affiliations:
- Youtu Lab
- Keen Security Lab
- Workbuddy
- Yunding Security Lab
arxiv_id: '2607.20911'
url: https://arxiv.org/abs/2607.20911
pdf_url: https://arxiv.org/pdf/2607.20911
published: '2026-07-22'
collected: '2026-07-24'
category: Agent
direction: Agent 编码智能体能力评估
tags:
- Agent
- Benchmark
- CodingAgent
- Evaluation
- ContaminationResistant
one_liner: 构建覆盖代码/网页/办公/安全4域的抗污染开源编码Agent评估基准与跨模型榜单
practical_value: '- 业务Agent评估可复用其抗污染任务构建思路：从真实业务场景反向改写任务为口语化请求，不直接复用公开问题，避免测试集被模型记忆导致评估失真

  - 多域Agent的统一评估框架可直接复用：自包含任务目录格式、沙箱隔离执行、后置校验的设计，适合内部运营/数据分析/客服等业务Agent的能力评测，无需重复搭建评估底座

  - 混合打分机制可迁移到非结构化输出评估：确定性规则+证据grounded LLM Judge加权组合、交互式任务用Agent Judge的思路，可直接用于电商文案生成、活动页生成、推荐理由生成等场景的效果评估'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有编码Agent基准存在两类核心问题：公开静态数据集的任务、解决方案多可通过网络检索获取，模型高分可能来自记忆而非真实推理能力，且覆盖场景单一；厂商闭源基准不可复现、存在偏向自有模型的选择偏置，无法满足真实工作中编码Agent跨多域处理任务的评估需求。

### 方法关键点
- 任务从真实commit、PR、业务场景反向工程改写为口语化角色扮演请求，不直接复用公开问题文本，从根源阻断prompt可被搜索的污染路径，配合版本迭代管理后续暴露风险
- 覆盖4个任务域：80个仓库级代码任务、70个前端开发交互任务、50个多文件办公流程任务、60个红蓝队安全任务，统一用自包含目录格式打包，沙箱隔离执行，评估资产在Agent完成任务后才加载
- 各域采用适配的打分机制：代码用隐藏单测、网页用规则+VLM/Agent Judge、办公用规则+LLM Judge、安全全deterministic打分，不做跨域分数平均，避免不合理的综合排序

### 关键结果
在双Agent Harness（CodeBuddy Code、Claude Code）下测试7款主流大模型，Claude Opus以75.0%总体得分排名第一，GLM-5.2、GPT-5.5分别以72.9%、72.0%位列二三位，各模型在不同域表现差异显著，无模型能在所有域领先。

最值得记住的一句话：Agent评估的核心是贴合真实工作流，抗污染要靠任务构建层面的设计，而非数据集保密。
