---
title: 'Activity Frames: Deterministic Screen-Activity Compilation for Agent Memory
  and Replay'
title_zh: Activity Frames：面向Agent记忆与回放的确定性屏幕活动编译框架
authors:
- Nossa Iyamu
affiliations:
- Independent Researcher
arxiv_id: '2608.05784'
url: https://arxiv.org/abs/2608.05784
pdf_url: https://arxiv.org/pdf/2608.05784
published: '2026-08-05'
collected: '2026-08-07'
category: Agent
direction: Agent 端侧 episodic memory 构建
tags:
- Agent Memory
- Episodic Memory
- Deterministic Compilation
- Routine Replay
- Screen Capture
one_liner: 无需模型参与的确定性屏幕活动编译流水线，生成可缓存可审计的Agent episodic memory
practical_value: '- 端侧用户行为记忆构建可参考两层架构：实测事实层采用纯规则确定性生成，彻底避免LLM摘要的幻觉与非确定性，大幅降低记忆生成成本；上层推理结果强制绑定置信度与证据链，可审计性大幅提升

  - 高频重复操作的成本优化可直接复用Routine Overhead Ratio测算方法：从用户行为日志中挖掘可复用操作序列，预编译为无模型依赖的回放脚本，可降低Agent执行重复任务的token成本最高343倍

  - 长上下文压缩可参考纯规则会话分割+结构化输出思路：将用户全天行为原始数据压缩86倍至2k token以内，mid-tier LLM使用该压缩上下文的问答准确率可追平frontier
  LLM，大幅降低推理成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有计算机使用Agent的记忆仅记录用户对话，无法感知用户实际操作行为。已有的屏幕捕获数据存在两个极端问题：直接投喂原始数据给LLM会导致token成本极高、超出上下文窗口；使用LLM做摘要则存在非确定性、幻觉、不可审计的缺陷，无法作为Agent的可信记忆源。
### 方法关键点
- 两层架构设计：第一层为纯规则生成的实测事实层，输出活动帧（包含应用、站点、起止时间、输入量、原始证据指针等字段），完全可复现、可缓存、可审计；第二层为可选推理层，所有推理结果必须带命名空间、置信度、关联证据，可随时剥离回纯事实层。
- 确定性编译规则：基于驻留时间上限90s、会话间隔阈值300s、20s内闪切合并三大规则对屏幕快照流做会话分割，无任何学习组件，输出字节级一致。
- 纯规则实体映射：通过URL解析规则生成页面类型（如搜索、PR、邮件等），无需模型参与，覆盖绝大多数主流站点场景。
### 关键结果
在单用户51天128756帧行为语料上测试：
1. 单天行为数据编译仅需68ms，生成的prompt友好上下文块比原始数据小86倍（仅1469 token）。
2. 基于编译上下文的用户行为问答准确率达98.4%，显著高于LLM摘要的66%~80%，mid-tier LLM效果可追平frontier LLM。
3. 编译生成的可复用操作回放脚本相比Agent从头推导routine的token成本降低60~343倍，单用户可复用routine出现率为9.0%（样本内）、7.7%（样本外）。
### 核心结论
Agent记忆构建的核心需求是可信、低成本、可复现，纯规则确定性编译在结构化行为记忆场景的性价比远高于依赖LLM的端到端方案。
