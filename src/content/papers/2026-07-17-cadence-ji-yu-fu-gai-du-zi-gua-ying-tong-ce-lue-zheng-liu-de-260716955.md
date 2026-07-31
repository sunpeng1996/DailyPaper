---
title: 'CADENCE: Closing the Reasoning Gap via Coverage-Adaptive On-Policy Distillation'
title_zh: CADENCE：基于覆盖度自适应同策略蒸馏的小模型推理能力提升
authors:
- Satyam Kumar
- Saurabh Jha
arxiv_id: '2607.16955'
url: https://arxiv.org/abs/2607.16955
pdf_url: https://arxiv.org/pdf/2607.16955
published: '2026-07-17'
collected: '2026-07-31'
category: Training
direction: LLM蒸馏 · 小模型推理能力优化
tags:
- KnowledgeDistillation
- OnPolicyTraining
- SmallLLM
- Reasoning
- LoRA
one_liner: 针对同策略蒸馏三类核心缺陷，提出6项针对性改进，单消费级设备即可实现60%+师生推理gap闭合
practical_value: '- 端侧/低延时场景小模型蒸馏可复用整体框架：电商搜索/推荐Agent需要部署低延时小模型时，可直接复用COVA自适应调度、FTB高熵token加权等组件，快速把大模型的推理能力迁移到小模型，降低推理成本

  - 稀疏奖励场景可借鉴CCD部分奖励设计：电商推荐RLHF流程中用户反馈稀疏时，可参考数值 proximity 思路给加购、收藏等接近转化的行为分配部分奖励，缓解奖励稀疏问题，提升训练效率

  - 关键位置训练可复用FTB加权思路：query理解、排序模型训练时，给高不确定性的token（如用户模糊query的关键分词、排序模型的特征交叉关键节点）分配更高训练权重，提升核心位置预测准确率

  - 中小团队可复用低成本训练配置：用LoRA+单消费级GPU的训练方案，无需算力集群即可完成定制化小模型蒸馏，大幅降低小业务场景的LLM落地门槛'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有同策略蒸馏是将大模型推理能力迁移到小模型的核心路径，但存在三类机制性缺陷：冷启动时小模型对大模型偏好token概率接近0，梯度消失无法学习推理模式；仅按训练步数插值正反KL的调度策略忽略不同prompt的覆盖度差异，易出现欠拟合或过拟合；二元对错奖励浪费部分正确轨迹的信息，奖励稀疏导致训练效率低，严重限制了小模型在低延时/端侧场景的落地效果。

### 方法关键点
- 基础框架DRIFT：逐token混合正反KL代理目标，基于学生采样轨迹计算梯度，避免序列级KL的高计算成本
- 6项核心改进：①COVA覆盖度自适应β调度，达到覆盖度阈值后加速正反KL切换；②FTB分叉token增强，给高教师熵的位置加权梯度，聚焦推理关键节点；③CCD密集奖励，给数值接近正确的错误轨迹分配部分奖励，非零奖励占比从38%提升到55%；④LAP简洁偏好强化，给更短的正确响应更高权重，降低推理耗时；⑤EMR熵匹配正则，提升模型校准度；⑥BSD自举自蒸馏，训练后对高一致性正确轨迹做SFT
- 2项稳定机制：教师强制热身、KL信任域，避免训练崩溃

### 关键结果
在GSM8K、MATH-500数据集上验证：0.5B学生模型蒸馏1.5B教师时，GSM8K pass@1从48.7%提升至69.8%，闭合63.2%师生gap；蒸馏3B教师时达到72.1%，闭合76.2%gap，比最强同算力基线高4.4个百分点。所有实验仅在单台Apple Mac Studio上运行，无需数据中心级算力。

针对性解决同策略蒸馏的机制性缺陷，即可用极低算力成本实现小模型推理能力的大幅提升，为端侧LLM落地提供了可复现的低成本路径。
