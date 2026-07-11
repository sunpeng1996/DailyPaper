---
title: 'Log-Insight: Automating Microservice Incident Diagnosis via Neuro-Symbolic
  Log Analysis'
title_zh: Log-Insight：基于神经符号日志分析的微服务故障自动诊断
authors:
- Carlos Garcia-Hernandez
- Aymane Abdali
- Guangyu Wu
- Mingxue Wang
- Fei Shen
- Zhaoyu Pang
- Yanbin Zhang
affiliations:
- Huawei Ireland Research Centre
- Huawei Dongguan R&D Centre
arxiv_id: '2607.08529'
url: https://arxiv.org/abs/2607.08529
pdf_url: https://arxiv.org/pdf/2607.08529
published: '2026-07-09'
collected: '2026-07-11'
category: Other
direction: LLM落地 · 神经符号长上下文压缩
tags:
- Log-Analysis
- Neuro-Symbolic
- Root-Cause-Analysis
- LLM-Application
- Microservice
one_liner: 华为提出结合符号日志预处理与LLM的微服务故障自动诊断系统，解决海量日志导致的LLM上下文溢出问题
practical_value: '- 长上下文场景可复用「符号预处理压缩+LLM生成」架构，先通过规则/统计方法过滤无关信息、保留核心信号，大幅降低LLM上下文压力，避免溢出和幻觉，可迁移至电商海量用户行为分析、推荐系统全链路异常排查等场景

  - 业务向LLM落地可模仿还原专家人工工作流的设计思路，先将人类专家的标准化操作拆解为可自动化的符号步骤，再交给LLM做最终合成，提升结果可解释性和业务接受度

  - 大流量日志/行为数据的异常分析场景，可复用其采样-聚类-熵导向压缩-对比偏移分析的预处理pipeline，在保留统计显著性信号的前提下实现千倍级数据压缩'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
大规模微服务故障排查时，单30分钟窗口可产生200万+日志行，远超LLM上下文窗口，现有方案分别存在缺乏语义推理、黑盒输出、上下文溢出、领域幻觉等缺陷，无法满足生产级根因分析需求。
### 方法关键点
复现SRE人工排查工作流，设计六阶段pipeline：两次采样、Schema推理与记忆、Drain3模式聚类、双层熵导向压缩、对比偏移分析、生成式合成，先通过符号处理将原始日志压缩1000~7000倍，仅保留高价值异常证据后交给LLM生成排序后的根因假设报告。
### 关键结果
在11个历史生产故障（110次运行，SRE标注真值）上MRR达0.790，90%以上运行中正确根因出现在Top3假设中，端到端延迟小于1分钟，明示日志模板和偏移统计的证据模块大幅提升了业务方接受度。
