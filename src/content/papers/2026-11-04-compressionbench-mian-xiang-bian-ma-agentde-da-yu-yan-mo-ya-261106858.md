---
title: 'CompressionBench: How can your coding agents compress LLMs?'
title_zh: CompressionBench：面向编码Agent的大语言模型压缩基准
authors:
- Xinrui Zhong
- Zhifeng Li
- Zhiming Wang
- Yongqi Liu
- Shanglin Yang
- Yang Zhou
- Zikun Li
- Zhuoming Chen
- Beidi Chen
affiliations:
- InfiniAI Lab
- Carnegie Mellon University
arxiv_id: '2611.06858'
url: https://arxiv.org/abs/2611.06858
pdf_url: https://arxiv.org/pdf/2611.06858
published: '2026-11-04'
collected: '2026-11-05'
category: Agent
direction: Agent能力评测 · LLM压缩
tags:
- Coding Agent
- LLM Compression
- Benchmark
- Quantization
- Model Efficiency
- Autonomous Optimization
one_liner: 构建编码Agent LLM压缩任务基准，验证Agent自主完成LLM压缩的可行性
practical_value: '- 电商/推荐场景自研轻量LLM做文案生成、语义匹配时，可复用本文压缩校验逻辑：除PPL外必须加下游业务指标（如文案点击率、语义匹配准确率）+推理稳定性校验，避免压缩后模型看似达标但业务效果下降

  - 开发工程类Agent（如自动调优推荐模型、特征工程）时，可复用本文的任务框架：固定资源/时间预算+分层反馈（局部低成本校验+全局高成本验证）+最终多维度验收的设计，大幅提升Agent任务成功率

  - 落地LLM压缩降本时，可直接复用固定存储优化trick：通过调整量化clip范围、按层/组件敏感度分配比特位、优化校准数据分布，能在不增加存储开销的前提下降低3%+的PPL损失，无需额外算法研发

  - 中小团队做LLM部署优化时，可引入编码Agent自动完成场景化压缩，效果优于通用公开量化工具，能大幅减少人工调优的人力投入'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM推理成本受内存访问瓶颈限制，压缩是降低部署成本、适配端侧/小显存硬件的核心手段，但传统压缩方案需要专业人员大量人工调优，难以快速适配任意存储约束和硬件目标。当前编码Agent已能承担复杂工程研发任务，亟需验证其能否自主完成符合资源约束的LLM压缩，为自动化模型优化、递归自改进提供落地路径。
### 方法关键点
- 定义LLM压缩为终端任务：给定源模型checkpoint、存储上限、GPU环境、8小时时间预算，Agent可自主选择量化、剪枝、低秩分解、蒸馏等任意压缩算法，最终输出压缩权重+可执行推理代码
- 分层反馈设计：搜索阶段提供完整模型PPL反馈，Agent自主决定是否做局部低成本验证（如权重重构误差）或全局高成本测试，平衡实验效率与准确性
- 多维度验证规则：最终提交需同时满足：包大小/GPU驻存大小双约束、下游任务准确率不低于BF16的80%、代码完整性校验，全部通过才记为有效
### 关键实验结果
测试6款主流编码Agent在3个源模型（2个MoE、1个稠密）+2种存储约束共6个任务上的表现，对比Baseline包括通用GPTQ、公开预量化版本（Unsloth Dynamic GGUF、GSQ-RCO等）：
- 36次提交中29次通过验证，宽松存储约束下18次提交全部通过
- 每任务选最优Agent方案，平均PPL仅比BF16高3.4%，下游准确率达77.33%（BF16为79.56%），效果优于所有公开预量化版本
- 固定存储开销下，21/24的迭代可进一步降低PPL，全局模型反馈可纠正17/79的局部指标排序错误
### 核心结论
LLM压缩效果不能仅凭PPL单一指标判断，数值设计、实验判断、可执行产物验证三者缺一不可
