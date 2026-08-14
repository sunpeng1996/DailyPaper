---
title: 'AutoDesign: Meta-Harness Optimization for Long-Horizon Agentic Design'
title_zh: AutoDesign：面向长周期智能体设计的元支架优化框架
authors:
- Yaxin Luo
- Haobin Jiang
- Jialv Zou
- Xu Huang
- Wenhao Yan
- Haodong Li
- Zhengrong Yue
- Jing Li
- Xiaofu Chen
- Xiaohan Zhao
affiliations:
- Meituan
- MBZUAI
- Huazhong University of Science and Technology
- Peking University
- Tsinghua University
arxiv_id: '2608.13560'
url: https://arxiv.org/abs/2608.13560
pdf_url: https://arxiv.org/pdf/2608.13560
published: '2026-08-12'
collected: '2026-08-14'
category: Agent
direction: Agent 长周期任务支架优化
tags:
- Long-Horizon Agent
- Meta-Optimization
- Harness Optimization
- Multimodal Generation
- Agent Evaluation
one_liner: 通过嵌套内外环元支架优化在不动模型参数前提下迭代升级设计系统，在论文转海报任务上超越商用方案
practical_value: '- 做Agent系统优化时可复用「不动模型参数、仅迭代外层支架」的思路，避免频繁微调大模型带来的成本和不稳定问题，尤其适合内容生成、商品素材生成这类业务场景

  - 可借鉴嵌套双环架构：内环处理单次任务生成+反馈修正，外环基于多任务轨迹迭代升级系统规则/工具/流程，适合电商商品详情页生成、营销文案批量生产这类标准化长周期生成任务

  - 系统迭代的验收门机制可直接复用：仅同时满足训练集性能提升、验证集性能不下降的更新才上线，能有效避免过拟合到少数业务case，保证系统稳定性

  - 多维度混合评估范式（规则校验+VLM打分+人工盲评）可迁移到生成式推荐的物料质量评估场景，兼顾效率和人类偏好对齐'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多模态设计系统的工作流是静态的，仅能针对单次输出做反馈修正，无法把人类设计偏好、成功经验沉淀为可复用的系统能力，长周期任务表现差且难以持续迭代。

### 方法关键点
- 采用嵌套双环架构：内环为设计支架，通过「设计者Agent+规则校验器+VLM评论家」的组合完成单次多模态输入到输出的迭代生成，输出全程保持可编辑格式，支持局部修改而非全量重生成
- 外环为元支架优化器，基于多轮任务的执行轨迹、评分结果，每次仅修改设计支架的5个功能组件（上下文/工具/运行时/编排/评估）之一，避免多变量改动导致的归因困难
- 设计严格的验收门机制：仅当更新后的支架在训练集上得分提升、且验证集得分不下降时才生效，防止过拟合；支持可选的人在回路引导，解决优化停滞问题

### 关键结果
- 构建跨5个学科的100篇论文PosterBench基准及10篇的mini子集，评估覆盖忠实度、布局、可读性等7个维度
- 主赛道得分78.32，比商用系统Claude Design高7.45分；接入优化后的设计支架后，7种不同编码Agent的平均得分从54.99提升到67.39，最高涨幅达19.6分
- 盲测人类偏好胜率达64%，单张海报生成仅需40分钟、成本低于3美元，达到会议级人类海报质量

最值得记住的结论：对落地级Agent系统来说，外层支架的迭代优化和底层模型能力提升同等重要，前者能在不改动模型的前提下大幅降低落地成本、提升业务表现
