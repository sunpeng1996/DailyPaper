---
title: Towards Identity-Preserving LLM Agents under Model Transition
title_zh: 模型切换场景下LLM Agent身份一致性保持的实证研究
authors:
- Yihuang Kang
- Pei-Cing Huang
- Chan-Tung Ku
- Chan Hsu
- Pei-Ju Lee
- I-Ling Cheng
affiliations:
- National Sun Yat-sen University
- National Chung Hsing University
arxiv_id: '2611.10628'
url: https://arxiv.org/abs/2611.10628
pdf_url: https://arxiv.org/pdf/2611.10628
published: '2026-11-07'
collected: '2026-11-10'
category: Agent
direction: LLM Agent 跨模型身份一致性评估
tags:
- LLM Agent
- Identity Drift
- Model Transition
- Compliance Testing
- Say-Do Gap
one_liner: 跨12个合规领域5760次测试证实LLM Agent换模型时相同外部状态无法确保身份一致
practical_value: '- 电商客服、导购、合规审核类Agent升级/切换后端模型时，不能仅验证口头承诺合规，必须搭建覆盖常见压力场景（如用户诱导违规、特殊权限申请等）的实测流程，避免Say-Do
  Gap导致的合规风险

  - Agent的persona、规则、历史记忆等外部配置的效果是模型依赖的，不要假设同一份配置在不同模型上效果一致，切换模型后需重新评估配置有效性，针对性调整prompt或记忆内容

  - 可直接复用本文的评估流程：先测同模型两次重加载的行为方差作为基线，再计算跨模型切换的行为漂移幅度，若漂移超过基线则判定不符合上线要求，大幅降低上线风险'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
生产环境中LLM Agent常因成本、性能要求切换/升级后端模型，从业者普遍默认复用相同persona、记忆、规则等外部状态即可保证Agent身份与行为一致，该假设缺乏实证验证，一旦发生行为漂移会引发合规事故、用户体验下降等严重问题。
### 方法关键点
- 定义Agent为(模型M、外部状态Σ、交互协议P)三元组，模型切换时固定Σ与P，将行为差异超过同模型重加载方差的情况定义为身份漂移
- 设计多维度评估体系：同时测量Say（口头合规承诺）、Do（压力场景下实际决策）、Say-Do Gap三个维度，采用独立L2模型做决策评审，避免自报告偏差
- 提出5组对比实验框架，覆盖重加载方差基线测试、跨模型漂移测试、外部状态效果测试、模型主导性测试、干预效果测试
### 关键实验
采用PACT基准的12个合规领域96个压力场景，测试GLM-5.3-Flash、Gemma4-31B、DeepSeek-V4.1-Flash三个开源模型，共5760次运行。核心结果：2/3的模型切换对出现显著身份漂移，幅度达2.5~3.3pp；仅GLM与DeepSeek切换时漂移<0.7pp，在重加载方差范围内；所有模型100%给出强合规口头承诺，但实际压力下合规率差达3.3pp，Say-Do Gap在2.9%~6.2%之间；外部状态Σ仅对Gemma有5.8pp的合规提升，对其余两个模型无显著效果。
### 核心结论
LLM Agent模型切换不是透明的基础设施操作，必须针对具体模型配对做行为级实证测试，仅靠口头验证会完全漏检身份漂移
