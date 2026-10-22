---
title: 'ATEST: Adaptive Resource-Aware Test-Time Scaling for LLM Inference'
title_zh: ATEST：面向LLM推理的自适应资源感知测试时缩放框架
authors:
- Mobina Kashaniyan
- Ali Jannesari
affiliations:
- Iowa State University
arxiv_id: '2610.25519'
url: https://arxiv.org/abs/2610.25519
pdf_url: https://arxiv.org/pdf/2610.25519
published: '2026-10-17'
collected: '2026-10-22'
category: LLM
direction: LLM推理优化 · 资源感知采样
tags:
- Test-Time Scaling
- LLM Inference
- GPU Resource Management
- Adaptive Sampling
- Energy Efficient
one_liner: 提出面向LLM推理的双模式资源感知测试时缩放框架，动态调采样预算兼顾精度、能耗与服务覆盖率
practical_value: '- 电商在线Agent、生成式推荐/答疑场景优先用ATEST-Online逻辑：先判断当前采样结果的投票稳定性，再结合实时GPU负载决策是否继续采样，在共享GPU集群下可实现0拒答，兼顾精度与能耗约束

  - 批量生成商品标签、文案等稳定负载的离线LLM任务，可选用ATEST-Calibrated模式，提前做1次数据集校准，即可获得更低尾延迟与更高吞吐量

  - 复用RLS在线更新成本模型+安全余量的设计，无需昂贵的离线数据集校准，即可快速适配新模型、新GPU、新业务场景，大幅降低上线预处理成本

  - 业务侧评估LLM推理服务效果时，建议将请求拒答率计入准确率计算，避免为了降本牺牲服务覆盖率，符合在线业务高可用要求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Test-Time Scaling（TTS，通过多采样投票提升LLM推理精度）普遍采用固定采样预算，忽略两个核心问题：不同query的推理难度差异大，且共享GPU上相同采样量的能耗随负载波动最高可达4.1倍。现有自适应采样方法仅关注推理精度优化，不感知实时GPU资源成本，容易导致高负载下能耗超标、大量请求被拒答。
### 方法关键点
- 双模式架构：①ATEST-Online（默认）：无需离线校准，从1个样本开始迭代采样，通过蒙特卡洛模拟判断当前投票结果的稳定性，用递归最小二乘法（RLS）在线学习实时GPU采样能耗，叠加安全余量后判断是否继续采样；②ATEST-Calibrated（离线）：提前对目标数据集做一次校准，构建固定的精度与成本预测模型，一次性确定单query采样预算，适合负载稳定的场景。
- 核心决策逻辑：同时评估新增采样的精度增益与当前GPU的实际能耗成本，仅当收益能耗比超过阈值时才继续采样，严格控制总能耗不超标。
### 关键实验
在A100、L40S GPU上测试Phi-3-mini、Qwen2.5-3B模型，覆盖GSM8K、MATH等4个推理数据集，对比Fixed-4、Adaptive-Cal等基线：①ATEST-Online在变负载下请求拒答率为0，精度达最优或统计持平，高负载下GSM8K精度达60.0%，比Calibrated模式高16个百分点；②包含校准成本时，Online模式比Calibrated模式少用42×GPU时间、48×能耗；③仅在负载长期稳定时，Calibrated模式精度略优、尾延迟更低。
### 核心结论
共享GPU上的测试时缩放不仅是推理精度问题，更是runtime资源管理问题，需同时权衡推理价值与实时资源成本。
