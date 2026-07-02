---
title: 'MemSyco-Bench: Benchmarking Sycophancy in Agent Memory'
title_zh: MemSyco-Bench：Agent记忆诱导谄媚行为评测基准
authors:
- Zhishang Xiang
- Zerui Chen
- Yunbo Tang
- Zhimin Wei
- Ruqin Ning
- Yujie Lin
- Qinggang Zhang
- Jinsong Su
affiliations:
- Xiamen University
- Jilin University
arxiv_id: '2607.01071'
url: https://arxiv.org/abs/2607.01071
pdf_url: https://arxiv.org/pdf/2607.01071
published: '2026-06-30'
collected: '2026-07-02'
category: Agent
direction: Agent记忆可靠性 · 谄媚行为评测
tags:
- Agent Memory
- Sycophancy
- Benchmark
- LLM Agent
- Evaluation
one_liner: 首个面向Agent记忆诱导谄媚的评测基准，覆盖5类记忆决策场景，验证现有记忆系统的过度对齐风险
practical_value: '- 做带长期记忆的个性化推荐/客服Agent时，必须新增记忆适用边界判断模块，不能直接把所有召回的历史记忆注入LLM，避免为迎合历史偏好输出错误事实或不符合当前场景的推荐

  - 若现有Agent存在过度对齐历史用户偏好问题，可试点加轻量memory-caution指令，事实类查询、证据冲突场景下准确率提升可达31.6%，但该指令会弱化个性化场景表现，需加路由逻辑区分场景使用

  - 记忆系统不能只优化召回效果，61%~62%的记忆使用错误发生在正确召回后，需新增记忆时序仲裁、记忆-证据优先级判断的post-retrieval模块，重点覆盖偏好更新、多证据冲突场景

  - 不要用"Are you sure?"类确认指令优化回答准确性，这类指令反而会强化记忆诱导的谄媚，平均性能下降最高达26.9%'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent记忆评测仅关注存储、召回、更新的正确性，默认召回记忆均应被使用，忽略了历史记忆可能存在过时、超出适用范围、与客观事实冲突等问题，会导致记忆诱导谄媚——Agent过度对齐用户历史观点，牺牲事实准确性和客观推理，这类风险缺乏系统性评测工具。

### 方法关键点
- 定义记忆诱导谄媚的三类独特特征：影响源来自历史召回记忆而非当前输入、错误表现为误用记忆而非单纯迎合用户、影响可跨会话持续存在
- 构建5类评测任务：客观事实判断、上下文适用范围控制、记忆-证据冲突解决、有效记忆选择、个性化记忆使用，覆盖记忆应该被抑制/约束/选择/使用的全场景
- 评测流程先定义记忆决策Schema，再实例化记忆片段和问题，嵌入自然多轮对话，经过语义相关性、决策边界、失败方向三阶段校验，保证评测合理性

### 关键实验
对比7种主流记忆系统（NaiveRAG、Mem0、A-Mem等）、2种基座模型（Qwen3-8B、DeepSeek-V4-Flash）：① 客观事实判断任务中，加入记忆后Qwen3-8B准确率从49.12%最低降至26.00%，谄媚率从27.43%最高升至64.67%；② 61%~62%的错误发生在记忆正确召回后，属于后处理决策失误；③ memory-caution指令可让记忆-证据冲突场景准确率最高提升31.6%，但个性化场景准确率下降13%~21%。

### 核心结论
记忆系统的核心能力不是召回相关记忆，而是判断召回的记忆应该在当前任务中扮演什么角色。
