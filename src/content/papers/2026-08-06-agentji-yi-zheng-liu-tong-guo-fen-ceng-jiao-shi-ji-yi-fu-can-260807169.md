---
title: 'Agent Memory Distillation: Empowering Small LLM Agents with Hierarchical Teacher
  Memory'
title_zh: Agent记忆蒸馏：通过分层教师记忆赋能小参数LLM Agent
authors:
- Taeil Kim
- Kangsan Kim
- Sung Ju Hwang
affiliations:
- KAIST
- DeepAuto.ai
arxiv_id: '2608.07169'
url: https://arxiv.org/abs/2608.07169
pdf_url: https://arxiv.org/pdf/2608.07169
published: '2026-08-06'
collected: '2026-08-11'
category: Agent
direction: Agent 分层记忆蒸馏 · 小模型知识迁移
tags:
- Agent
- Knowledge Distillation
- Memory System
- Small LLM
- Tool Use
one_liner: 提出训练免的分层记忆蒸馏框架，将大模型Agent成功经验迁移给小模型提升任务性能
practical_value: '- 电商垂类小Agent（客服/导购/工具调用类）可直接复用这套训练-free方案，用大模型生成的成功轨迹蒸馏三层记忆，无需微调即可大幅提升4B/8B小模型性能，降本增效

  - 记忆分层设计可直接落地：任务级策略用自然语言存储保证泛化性，子步骤/工具调用存可执行示例（如API模板、召回规则片段），主动注入前两种记忆，仅报错时召回工具记忆，避免上下文膨胀

  - 小模型记忆检索选k=1即可达到最优效果，无需多候选召回，既降低算力消耗，也避免多余记忆引入噪声干扰小模型推理

  - 4B级小模型从该方案获得的增益最大，低延迟/边缘部署的推荐、客服场景优先给4B模型适配该方案ROI最高'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent记忆方案大多适配大参数模型，小LLM自身任务成功率低，生成的记忆库以失败轨迹为主价值极低；直接搬运大模型的记忆又因大小模型能力差，小模型无法理解吸收，增益微乎其微，亟需适配小模型的低成本知识迁移方案。
### 方法关键点
- 完全训练-free，不修改小模型参数，仅通过记忆迁移实现能力提升
- 从大模型教师的成功轨迹中拆分三层互补记忆：Workflow记忆存储任务级抽象策略（自然语言，脱敏具体参数保证泛化性）；Subtask记忆存储子任务级具体执行示例；Function记忆存储单工具的调用规则、常见坑和成功案例
- 记忆注入逻辑：任务启动前主动将Workflow和Subtask记忆注入系统提示词，仅当工具调用报错时才召回对应Function记忆追加到上下文，避免无效占用上下文窗口
### 关键实验
在AppWorld、BFCL V3、ToolSandbox三个工具调用基准上测试，以GPT-5-mini为教师，4个4B~8B小模型为学生，对比Zero-shot、ReasoningBank等基线：平均准确率增益分别为27.2%p、11.2%p、3.4%p，部分学生模型准确率超过教师；4B级模型增益最高，Subtask记忆贡献最大，检索k=1效果最优。
### 核心结论
小模型Agent知识迁移的核心不是直接堆叠大模型经验，而是要按小模型的理解能力做分层结构化的记忆设计，训练-free的方案也能让小模型追平甚至超过大教师的性能
