---
title: 'Rules, Traces and Routing Statistics: Training and Calibration Data for Open
  Models on ARC-AGI-2'
title_zh: 面向ARC-AGI-2开放模型的训练校准数据：规则、轨迹与路由统计
authors:
- Nguyen Minh Thang
- Trinh Thi Phuong
affiliations:
- VNU University of Science, Vietnam
arxiv_id: '2611.06827'
url: https://arxiv.org/abs/2611.06827
pdf_url: https://arxiv.org/pdf/2611.06827
published: '2026-11-04'
collected: '2026-11-05'
category: Reasoning
direction: 大模型推理优化 · 训练数据与部署工程
tags:
- MoE-pruning
- reasoning-traces
- ARC-AGI
- KV-cache
- fine-tuning
one_liner: 4张L4 12小时约束下通过数据与推理优化将ARC-AGI-2得分最高提至56.67
practical_value: '- 业务微调优先投入真实标注数据：本实验验证海量合成数据训练效果远低于少量高质量真实业务数据，不要盲目堆合成数据规模

  - MoE推荐大模型部署显存不足时，可基于业务请求的路由统计剪枝冷门专家，配合FP8量化缓存大幅提升KV cache容量，基本无损精度

  - Agent/生成式推荐场景可在推理侧提效：服务层强制长思考链、生成结果先过校验规则、优先长首轮推理等策略，无需改模型即可提准

  - 多GPU部署推荐服务时，可给不同卡分配差异化上下文长度、任务按预估耗时排序调度，最大化硬件利用率降低超时率'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
ARC-AGI-2是衡量通用推理能力的核心基准，官方要求方案必须在4张L4 GPU、12小时离线无网的强资源约束下运行，此前公开最优得分仅24.03%，业内对训练校准数据、推理流程、部署优化的实际增益缺乏量化对比，容易做无效调优。
### 方法关键点
- 数据构建：生成12000条行为特征唯一的可执行规则语料，衍生95993条合成任务，过滤可通过捷径求解的低质量样本；收集模型自身答对的1036条推理轨迹，做拒绝采样微调
- MoE优化：针对Qwen3.8-Flash-Next 125B MoE模型，基于业务路由统计+激活显著性剪枝冷门专家，保留程序token相关专家，配合FP8索引缓存扩容KV cache
- 推理流程优化：服务引擎层强制开启thinking cap，输出Python程序后先在示例上校验，每个输入优先执行长首轮推理再尝试次轮
- 调度优化：任务按预估耗时排序分配，不同GPU设置差异化上下文长度，最大化12小时窗口的任务处理量
### 关键结果
在ARC-AGI-2 120条半私有隐藏任务上测试：
1. Qwen3-4B网格模型用1920条真实任务微调+调度优化，得分从28.96提升至33.06，所有合成数据训练方案均无增益
2. Qwen3.8-27B稠密模型配合推理流程优化，得分从26.81提升至44.03，超过无时间限制的base模型得分42.36，70%以上增益来自推理侧优化
3. Qwen3.8-Flash-Next 125B MoE剪枝至296专家/层，KV cache容量提升3.6倍，最终得分达56.67，为本次实验最优结果

最值得记住的结论：资源约束场景下，推理侧与调度优化的收益往往超过大模型微调甚至海量合成数据增量训练的收益，少量高质量真实业务数据的微调效率远高于大规模低质量合成数据。
