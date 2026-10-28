---
title: 'HABIT-Bench: Evaluating Habit Induction from Longitudinal Weak Evidence in
  Agent Memory'
title_zh: HABIT-Bench：面向Agent记忆的长时序弱证据习惯归纳评测基准
authors:
- Junming Zhang
- Rubin Wei
- Xu Cheng
- Hao Sun
- Jiarui Wang
- Ruoxi Cheng
- Xiquan Wang
- Peisong Wu
- Mingsong Chen
- Zhouhan Lin
affiliations:
- Shanghai Jiao Tong University
- Shanghai Artificial Intelligence Laboratory
- Fudan University
arxiv_id: '2610.24520'
url: https://arxiv.org/abs/2610.24520
pdf_url: https://arxiv.org/pdf/2610.24520
published: '2026-10-19'
collected: '2026-10-28'
category: Agent
direction: Agent 长时记忆用户习惯归纳评测
tags:
- LLM Agent
- Long-term Memory
- Habit Induction
- Benchmark
- Personalization
one_liner: 构建覆盖4个场景的评测基准，量化当前Agent记忆系统的用户习惯归纳能力差距
practical_value: '- 做个性化Agent/生成式推荐的长时用户建模时，不要盲目迷信复杂记忆管道，简单BM25/Dense RAG基线在多数场景下性能和A-MEM、Mem0等成熟记忆方案接近，可先验证基线效果再做增量优化

  - 用户习惯归纳需明确区分有效证据（用户确认的选择、重复稳定行为）和非绑定证据（未接受的系统建议、临时例外、过时偏好），电商/广告推荐场景可在用户行为标签体系中新增证据类型标注，减少过度个性化错误

  - 记忆系统选型要权衡构建成本和效果，论文显示A-MEM等方案的内存构建耗时是BM25 RAG的数百倍，查询成本相近，低频交互场景优先选用轻量检索方案ROI更高'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent长时记忆评测多聚焦历史事实召回、显式偏好匹配，未覆盖「从零散弱证据中归纳用户习惯、判断习惯适用边界（临时例外、时效、场景限制）」的复合能力评估，而这是长期交互型个性化Agent、生成式推荐系统的核心痛点，已有基准无法同时支持弱证据归纳、上下文门控、习惯漂移识别、过度个性化规避等多维度能力测试。
### 方法关键点
- 基于真实任务对话数据+可控习惯图生成114个虚拟用户的长时序交互历史，覆盖食品、金融、软件、旅行4个领域，共37152个会话、3328个四选一测试探针，探针包含习惯边界判断、临时例外处理、过时习惯区分、未接受建议过滤等难点
- 评测协议要求记忆系统按时间顺序消化会话，探针测试时仅能访问截止时间前的历史，用共享底座LLM做固定格式答案选择，指标采用领域平均准确率，避免LLM打分偏差
- 加入人工验证环节，抽样探针的证据可解释性，确保92%+的探针在提供标注证据时人类可唯一确定正确答案
### 关键实验结果
对比8种主流记忆方法（A-MEM、Mem0、Letta等）、5种检索基线、2种控制组，底座采用Qwen3-235B-A22B和GLM-5.3-Flash：
1. 最优记忆方法的四域平均准确率仅33.61%，仅比BM25 RAG高1.1个百分点，远低于Full Memory（压缩全历史喂给模型）的41.98%，仅比随机猜测（25%）高8.6个百分点
2. 就算直接给标注好的相关证据，模型准确率最高也仅58.25%，说明当前记忆系统的瓶颈不仅在检索，更在证据推理和习惯适用判断
### 核心结论
当前主流的Agent记忆方案并不能稳定优于简单检索基线，从长时序弱行为中归纳用户习惯并合理应用的能力仍存在巨大缺口
