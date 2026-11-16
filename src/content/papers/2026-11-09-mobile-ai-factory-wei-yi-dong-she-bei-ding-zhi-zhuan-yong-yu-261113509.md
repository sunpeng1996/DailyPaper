---
title: 'Mobile AI Factory: Building Specialized Language Models for Your Mobile Device'
title_zh: Mobile AI Factory：为移动设备定制专用小语言模型的代理系统
authors:
- Evan Li
- Krishna Deshpande
- Wen Cheng
- Shyamnath Gollakota
affiliations:
- University of Washington
arxiv_id: '2611.13509'
url: https://arxiv.org/abs/2611.13509
pdf_url: https://arxiv.org/pdf/2611.13509
published: '2026-11-09'
collected: '2026-11-16'
category: Agent
direction: Agent 端侧小语言模型自动化定制
tags:
- Agent
- SLM
- On-device LLM
- LoRA
- Quantization
- AutoML
one_liner: 首个自动生成适配特定任务与手机的微调量化SLM的代理系统，性能优于5-shot前沿大模型
practical_value: '- 端侧推荐/搜索业务可直接复用「硬件全配置预 profiling + 模型从小到大分桶搜索」框架，无需人工逐个机型适配，大幅降低端侧模型落地成本

  - 小模型自动微调流程可复用单步干预+回滚机制：每次迭代仅选择1种操作（调LoRA超参/挖真实数据/生成错误导向合成数据），效率比暴力搜索高19倍，适合业务快速迭代

  - 量化精度校验方法可直接落地：必须用目标推理引擎（llama.cpp/MNN等）导出的实际部署模型做评估，避免通用量化checkpoint导致的线上精度掉点（文中MNN默认4-bit最多掉0.19
  F1）

  - 端侧Agent选型不要依赖硬件spec推导性能，必须实测：哪怕Claude Opus 5.5给全参数，硬需求场景仍有60%概率选错配置，实测是唯一可靠的判断依据'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
端侧小语言模型（SLM）可保护用户隐私、无网络也能运行，但需要针对特定任务和手机做微调、量化、性能适配，传统人工适配成本极高；不同手机硬件差异大，同模型同配置在不同手机上的性能差可达94倍，前沿大模型也无法仅靠硬件参数准确判断适配性，亟需自动化方案。

### 方法关键点
- 代理架构：LLM编排器负责每次迭代选择1种干预操作（调整LoRA超参/挖掘真实训练数据/生成针对错误case的合成数据），固定规则负责回滚无效操作、控制模型升舱、管理训练预算，避免LLM决策不稳定问题
- 从小到大分桶搜索：将不同参数量+量化级别的模型按磁盘大小分为5个桶，优先搜小桶模型，当前桶精度无法提升时再切更大桶，平衡模型体积和精度
- 端侧预 profiling：每台手机提前测试全量（模型/量化级别/推理引擎/CPU/GPU后端）组合的延迟、内存、能耗数据，跨任务复用，仅搜索符合硬件约束的配置
- 自适应精度目标：以教师模型5-shot分数为基准（最低0.8），达标后可自动提升目标继续优化，避免固定目标过高或过低的问题

### 关键实验
在10个NLP任务（实体抽取、意图分类、摘要等）、4台不同档位安卓手机上测试：生成的端侧模型在5个任务上优于5-shot Claude Sonnet 5、DeepSeek v4 Flash，最高领先0.34，3个任务持平；实体抽取任务上比全量遍历27种模型配置节省19倍GPU时间，精度差仅0.03；无实测仅靠硬件参数选配置时，Claude Opus 5.5在硬需求场景有60%的配置不符合要求。

**最值得记住的一句话：** 端侧LLM适配没有银弹，硬件实测数据比任何推理和spec都可靠，自动化小模型定制的核心是「LLM做灵活决策+固定规则守边界+实测数据做约束」
