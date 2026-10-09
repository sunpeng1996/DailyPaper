---
title: 'Beyond the Parameter Monolith: Reconstructive Memories, Executable Skills,
  and Residual Assembly for Language Models'
title_zh: 《超越参数单体：面向语言模型的重构记忆与可执行技能架构》
authors:
- A. Bochkov
arxiv_id: '2610.04012'
url: https://arxiv.org/abs/2610.04012
pdf_url: https://arxiv.org/pdf/2610.04012
published: '2026-10-01'
collected: '2026-10-09'
category: LLM
direction: 大语言模型 · 模块化架构设计
tags:
- Modular LLM
- External Memory
- Tool Calling
- Residual Assembly
- Retrieval Augmentation
one_liner: 提出模块化FEM-ASM架构，拆分LLM的存储、执行与推理能力，验证各模块接口的有效性与局限性
practical_value: '- 设计工具调用类Agent（如电商价保计算、库存查询智能助手）时，优先采用位置感知的结果渲染接口，替代全局重复的结果向量，可大幅提升工具输出的准确率，参考论文中算术调用准确率从8.59%提升至100%的结论

  - 搭建企业级RAG系统（如电商商品知识库、客服问答系统）时，可复用模块化解耦思路：记忆单元、检索模块、生成核心独立迭代，知识库更新无需重训基座LLM，降低迭代成本

  - 优化外部记忆系统时，需拆分存储、寻址、内容提取、答案渲染四个独立问题单独优化，避免混淆问题根因：比如检索召回率达标不代表最终生成答案正确，需单独校验每个环节的指标'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Transformer类大语言模型将知识存储、逻辑推理、工具执行能力全部耦合在统一参数体系中，不同生命周期的组件（如动态更新的知识库、固定的算术工具、基座推理能力）无法独立迭代，故障难以定位，全链路重训成本极高。
### 方法关键点
1. 提出FEM-ASM模块化架构，拆分三类独立组件：重构记忆单元存储文档编码的局部状态，可执行技能单元实现确定性工具逻辑，神经协调核心通过残差组装机制融合两类外部单元的输出；
2. 重构记忆采用版本化不可变设计，支持独立更新、溯源，通过冻结Codec实现编码解码，无需重新训练核心模型即可新增记忆单元；
3. 可执行技能采用确定性操作数提取+位置感知结果渲染接口，降低工具调用的输出序列化误差；
4. 检索层采用固定前缀、滑动窗口、n-gram特征的候选生成+重排架构，避免语义检索的召回波动。
### 关键实验
基于FineWeb-Edu数据集训练：1.7B浮点值预算下可存储52809个重构记忆单元，token重建准确率约75%；算术工具调用实验中，位置感知渲染接口的训练集内准确率达100%，远高于全局重复向量方案的8.59%；特权坐标下检索模块top1召回达97.7%。
### 核心结论
存储、寻址、内容提取、答案渲染是四个完全独立的问题，模块化架构可大幅降低故障定位和迭代成本，无需全链路重训即可替换单个组件
