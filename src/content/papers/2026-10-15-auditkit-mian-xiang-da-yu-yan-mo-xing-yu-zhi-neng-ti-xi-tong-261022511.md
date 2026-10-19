---
title: 'AuditKIT: A Unified Evaluation Spine for Benchmarking, Judging, and Comparing
  Large Language Models and Agentic Systems'
title_zh: AuditKIT：面向大语言模型与智能体系统的统一评估框架
authors:
- Shreeyans Arora
- Utsav Avaiya
- Zera Lyngkhoi
- Hem Gosalia
- Ram Mohan Rao Kadiyala
- Vinay Kumar Sankarapu
- Pratinav Seth
affiliations:
- Lexsi Labs
arxiv_id: '2610.22511'
url: https://arxiv.org/abs/2610.22511
pdf_url: https://arxiv.org/pdf/2610.22511
published: '2026-10-15'
collected: '2026-10-19'
category: Eval
direction: LLM与智能体系统多维度统一评估
tags:
- LLM-Evaluation
- Agent-Evaluation
- RAG-Evaluation
- Tool-Use
- Benchmarking
- Reproducibility
one_liner: 开源统一评估库，整合LLM、Agent、RAG多维度评估能力，解决现有工具指标不统一问题
practical_value: '- 复用方向感知的指标定义规范，对齐业务中LLM/Agent/RAG的评估指标，避免因指标优化方向（如latency越低越好、准确率越高越好）混乱导致的选型错误

  - Agent工具调用评估的最大二分匹配、并行/串行调用区分逻辑可直接复用，解决电商智能客服、导购Agent的工具调用准确率评估问题，避免贪婪匹配导致的得分偏差

  - RAG评估的分层指标（检索质量+生成质量+确定性证据校验）可迁移到电商商品问答、售后咨询RAG系统的效果评估，同时区分召回和生成环节的问题

  - 多模型对比的配置指纹机制可复用，确保业务侧模型选型、版本迭代的评估实验可复现，避免因prompt、解码参数不一致导致的效果误判'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM、Agent、RAG的评估工具分散，接口、指标定义、结果格式不统一，存在指标优化方向不明确、工具调用评估忽略执行时序、缺失证据被误判为失败等问题，导致评估结果不可比、难以定位真实问题。

### 方法关键点
- 统一评估接口，将基准测试、LLM-as-Judge、性能profiling、工具调用评估、RAG评估整合到同一pipeline，输出标准化RunResult结构
- 强制每个指标声明MAXIMIZE/MINIMIZE方向，搭配配置全链路SHA-256指纹，确保多模型对比的正确性和实验可复现
- Agent评估引入轮次感知的工具调用最大二分匹配，区分并行/串行调用，将验证过的任务outcome与轨迹诊断分离，缺失证据标记为unscored而非失败
- RAG评估同时覆盖排序检索指标、生成事实性校验、确定性证据检查（如新鲜度、权限合规），支持分层定位问题

### 关键结果
7个案例覆盖模型选型、服务runtime、RAG、工具调用等场景，核心结果包括：1）答案提取规则会让SST-2任务上Llama-2-13B的准确率从0.58提升到0.91，直接改变模型排名；2）相同模型在不同serving runtime上的多语言答题准确率差异可达20%；3）工具调用评估中，Qwen2.5-14B比7B在无关请求拒答准确率上高12个百分点。

**最值得记住的一句话**：评估结论的可信度远不止于最终得分，必须同时对齐评估配置、证据来源、指标定义才能保证结果可比。
