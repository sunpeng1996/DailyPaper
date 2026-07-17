---
title: 'OmniaBench: Benchmarking General AI Agents Across Diverse Scenarios'
title_zh: OmniaBench：覆盖多元场景的通用AI Agent评测基准
authors:
- Chengyu Shen
- Yujie Fu
- Gangtao Xin
- Yanheng Hou
- Wenlong Fei
- Guojie Zhu
- Jiawei Li
- Hongcheng Gao
- Runming He
- Zhen Hao Wong
affiliations:
- Huawei Cloud
- Peking University
- Renmin University of China
- Beijing Institute of Technology
- Tsinghua University
arxiv_id: '2607.14989'
url: https://arxiv.org/abs/2607.14989
pdf_url: https://arxiv.org/pdf/2607.14989
published: '2026-07-16'
collected: '2026-07-17'
category: Agent
direction: Agent通用能力多场景评测基准
tags:
- Agent
- Benchmark
- LLM
- Tool Use
- Evaluation
one_liner: 构建覆盖354个细分领域、支持10维能力诊断的通用AI Agent多场景评测基准
practical_value: '- 可复用其10维Agent能力拆解框架，诊断电商导购、工单处理、运营自动化等业务场景下Agent的规划、约束遵守、错误恢复等短板，针对性迭代优化

  - 可借鉴其DAG/DAG-S/Solver/Program四条任务合成路线，自动生成业务场景Agent测试用例，大幅降低人工构造测试集的成本

  - 其用户模拟器+rubric自动评分的评测pipeline可直接复用在业务Agent的版本迭代评测中，减少人工评测的工作量

  - 从其错误分布结论可知，当前Agent核心瓶颈在长程规划、状态跟踪而非基础工具调用，业务Agent迭代可优先优化规划与状态管理模块，投入产出比更高'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Agent评测基准普遍存在场景覆盖窄、工具生态单一、交互形式固定的问题，无法系统刻画通用Agent在异构真实场景下的能力边界，难以匹配电商、企业服务等落地场景对多轮交互、动态状态跟踪、复杂工具编排的评测需求。
### 方法关键点
- 从应用商店、产品文档、行业资源、Web检索等渠道提取场景知识，构建覆盖ToC/ToB/ToE的分层领域分类体系，包含90个一级领域、354个二级领域，场景覆盖广度远超现有基准
- 基于领域分类构建带状态空间的可执行环境，通过DAG、DAG-S、Solver、Program四条互补路线合成单/多轮任务，配套10维能力分类、8个原子难度因子，支持细粒度能力诊断
- 采用VerifyCode+人工校准rubric的双轨评估规则，多轮任务引入persona驱动的用户模拟器，所有环境和任务均经过可执行性校验，结果可复现
### 关键结果
- 总数据集包含1431个任务，同步推出644个任务的高难度子集，兼顾评测覆盖度与成本效率
- 前沿闭源模型Claude-Sonnet-5、GPT-5.6-Sol的整体Pass@1仅为58.54%、57.14%，开源模型GLM-5.2达到56.83%，基准区分度极强
- 错误分析显示53.8%的失败来自推理问题，其中36.7%为规划分解错误、16.5%为约束违反，基础工具调用错误占比极低
### 核心结论
相同整体得分的Agent模型可能在不同领域、不同能力维度表现差异极大，当前通用Agent的核心瓶颈并非基础工具调用能力，而是长程规划、约束维护与基于执行反馈的自适应修正能力
